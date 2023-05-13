from flask import Blueprint, jsonify, request

from app.extensions.init_sqlalchemy import db
from app.models.model_user import UserBase
from app.utils.JWT import JWTManager
from app.utils.redis_db import redis_db

user_base = Blueprint('userBase', __name__, url_prefix='/user')


# 获取用户基本信息
@user_base.post('/info/')
def get_user_info():
    token = request.headers["Authorization"]
    if not token:
        # toekn为null，则表示用户没有登录，则无法获取基本信息
        return jsonify(success=False, msg="Token失效~")
    # 根据token获取用户的id
    token_data = JWTManager.verify_jwt(token)
    print("解析token得到的user_id={}".format(token_data))
    if token_data != "error":
        # 根据user_id查询得到用户基本信息并将数据返回
        user_base = UserBase.query.filter(UserBase.id == token_data.get("data").get("user_id")).first()
        if not user_base:
            return jsonify(success=False, msg="Token为错误token，请重新登录~")
        print("获取到的用户信息是{}".format(user_base))
        # 返回用户基本信息
        result = {
            'msg': '请求成功',
            'code': 200,
            'data': {
                'user_id': user_base.id,
                'username': user_base.username,
                'realname': user_base.realname,
                'avatar': user_base.avatar,
                'remark': user_base.remark,
                'enable': user_base.enable,
                'create_at': user_base.create_at
            }
        }
        return jsonify(result)
    else:
        return jsonify(success=False, msg="Token失效了又！")


@user_base.post("/regist_tourist/")
def regist_tourist():
    """
    游客注册接口
    :return:
    """
    # 获取用户的deviceId
    device_id = request.get_json()['device_id']
    if not device_id:
        return jsonify(success=False, msg="用户device_id为null")
    # 首先根据device_id查询是否存在该用户
    tourist_user = UserBase.query.filter(UserBase.deviceid == device_id).first()
    if not tourist_user:
        # 创建一个BaseUser对象
        tourist_user = UserBase(deviceid=device_id, enable=1)
        # 将数据添加到数据库中
        db.session.add(tourist_user)
        db.session.commit()
    # 为用户生成了一个token，同时将此内容存在redis中
    tourist_user = UserBase.query.filter(UserBase.deviceid == device_id).first()
    if not tourist_user:
        return jsonify(success=False, msg="创建游客用户失败")
    # 创建用户成功，获取用户id，同时根据用户id创建一个token，并将该token信息返回
    print(f"当前游客用户信息是{tourist_user}")
    # 根据用户id查询当前是否在redis中存在已经生成的token，如果存在，则直接返回，否则创建一个新的token
    # 只要重新执行了注册接口，就需要重新生成token
    tourist_token = JWTManager.generate_jwt_token(tourist_user.id)
    print("当前新生成的token是{}".format(tourist_token))
    # 将token和user_id数据添加到redis中
    redis_db.handle_redis_token(tourist_user.id, tourist_token)
    result = {
        'msg': '请求成功',
        'code': 200,
        'data': tourist_token
    }
    return jsonify(result)


@user_base.post("/update_avator/")
def update_avator():
    # 首先验证用户的token是否失效
    token = request.headers["Authorization"]
    if not token:
        # toekn为null，则表示用户没有登录，则无法获取基本信息
        return jsonify(success=False, msg="Token失效~")
    # 验证用户传递过来的头像
    avator_url = request.get_json()["avator_url"]
    if not avator_url:
        return jsonify(success=False, msg="传递的头像地址不正确~")
    # 根据token获取用户的id
    token_data = JWTManager.verify_jwt(token)
    print("解析token得到的user_id={}".format(token_data))
    if token_data != "error":
        # 根据user_id查询到对应的用户信息
        user_id = token_data.get("data").get("user_id")
        UserBase.query.filter(UserBase.id == user_id).update({'avatar': avator_url})
        db.session.commit()
        return jsonify(success=True, msg="更新头像成功")
    else:
        return jsonify(success=False, msg="用户token已失效~")


@user_base.post("/update_username/")
def update_username():
    # 首先验证用户的token是否失效
    token = request.headers["Authorization"]
    if not token:
        # toekn为null，则表示用户没有登录，则无法获取基本信息
        return jsonify(success=False, msg="Token失效~")
    # 获取用户新昵称
    username = request.get_json()["username"]
    if not username:
        return jsonify(success=False, msg="用户昵称为空，不能修改~")
    # 根据token获取用户的id
    token_data = JWTManager.verify_jwt(token)
    print("解析token得到的user_id={}".format(token_data))
    if token_data != "error":
        user_id = token_data.get("data").get("user_id")
        UserBase.query.filter(UserBase.id == user_id).update({'username': username})
        db.session.commit()
        return jsonify(success=True, msg="更新昵称成功")
    else:
        return jsonify(success=False, msg="用户token已失效~")


@user_base.post("/update_password/")
def update_password():
    # 首先验证用户的token是否失效
    token = request.headers["Authorization"]
    if not token:
        # toekn为null，则表示用户没有登录，则无法获取基本信息
        return jsonify(success=False, msg="Token失效~")
    # 验证用户传递过来的头像
    req_password = request.get_json()["password"]
    if not req_password:
        return jsonify(success=False, msg="传递密码不正确~")
    # 根据token获取用户的id
    token_data = JWTManager.verify_jwt(token)
    print("解析token得到的user_id={}".format(token_data))
    if token_data != "error":
        # 根据user_id查询到对应的用户信息
        user_id = token_data.get("data").get("user_id")
        user_base = UserBase.query.filter(UserBase.id == user_id).first()
        user_base.set_password(req_password)
        db.session.commit()
        return jsonify(success=True, msg="更新密码成功")
    else:
        return jsonify(success=False, msg="用户token已失效~")
