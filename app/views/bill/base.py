from flask import Blueprint, jsonify, request

from app.utils.JWT import JWTManager

bill_base = Blueprint('billBase', __name__, url_prefix='/bill')


# 获取用户基本信息
@bill_base.get('/list')
def get_user_info():
    # 首先验证用户的token是否失效
    token = request.headers["Authorization"]
    if not token:
        # toekn为null，则表示用户没有登录，则无法获取基本信息
        return jsonify(success=False, msg="Token失效~")
    # 分别获取当前传递过来的数据
    # 获取页码
    page = request.get_json()["page", 1]
    page_size = request.get_json()["page_size", 5]
    # 根据token获取用户的id
    token_data = JWTManager.verify_jwt(token)
    print("解析token得到的user_id={}".format(token_data))
    if token_data != "error":
        # 根据user_id查询到对应的用户信息
        user_id = token_data.get("data").get("user_id")
        # 根据用户id查询对应的账单数据

    return jsonify(success=True, msg="test")
