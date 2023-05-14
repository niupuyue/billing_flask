from flask import Blueprint, jsonify, request

from app.extensions.init_sqlalchemy import db
from app.models import UserBase, BillType, BillDetail
from app.utils.JWT import JWTManager
from app.utils.time_utils import get_start_and_end_timestamp_by_year_month

bill_base = Blueprint('billBase', __name__, url_prefix='/bill')


# 新增账单数据
@bill_base.post('/add/')
def add_bill():
    # 首先验证用户的token是否失效
    token = request.headers["Authorization"]
    if not token:
        # toekn为null，则表示用户没有登录，则无法获取基本信息
        return jsonify(success=False, msg="Token失效~")
        # 根据token获取用户的id
    # 获取传递的数据
    money_amount = float(request.get_json()["money_amount"])
    note = request.get_json()["note"]
    type_id = int(request.get_json()["type_id"])
    if not type_id or not money_amount:
        return jsonify(success=False, msg="参数不完整~")
    token_data = JWTManager.verify_jwt(token)
    print("解析token得到的user_id={}".format(token_data))
    if token_data != "error":
        # 根据user_id查询到对应的用户信息
        user_id = token_data.get("data").get("user_id")
        bill_detail = BillDetail()
        bill_detail.user_id = user_id
        bill_detail.money_amount = money_amount
        bill_detail.note = note
        bill_detail.type_id = type_id
        db.session.add(bill_detail)
        db.session.commit()
        return jsonify(success=True, msg="添加成功~")
    else:
        return jsonify(success=False, msg="Token失效了~")


# 删除账单
@bill_base.post('/delete/')
def delete_bill():
    # 首先验证用户的token是否失效
    token = request.headers["Authorization"]
    if not token:
        # toekn为null，则表示用户没有登录，则无法获取基本信息
        return jsonify(success=False, msg="Token失效~")
    # 获取传递的数据
    bill_id = int(request.get_json()["bill_id"])
    if not bill_id:
        return jsonify(success=False, msg="参数不完整~")
    token_data = JWTManager.verify_jwt(token)
    print("解析token得到的user_id={}".format(token_data))
    if token_data != "error":
        # 根据user_id查询到对应的用户信息
        user_id = token_data.get("data").get("user_id")
        bill_detail = BillDetail.query.filter_by(id=bill_id, user_id=user_id).first()
        if bill_detail:
            bill_detail.enable = 0
            db.session.commit()
            return jsonify(success=True, msg="删除成功~")
        else:
            return jsonify(success=False, msg="删除失败~")


# 获取用户全部账单信息
@bill_base.get('/list/')
def get_user_bill():
    # 首先验证用户的token是否失效
    token = request.headers["Authorization"]
    if not token:
        # toekn为null，则表示用户没有登录，则无法获取基本信息
        return jsonify(success=False, msg="Token失效~")
    # 分别获取当前传递过来的数据
    # 获取页码
    page = request.get_json()["page"]
    page_size = request.get_json()["page_size"]
    # 根据token获取用户的id
    token_data = JWTManager.verify_jwt(token)
    print("解析token得到的user_id={}".format(token_data))
    if token_data != "error":
        # 根据user_id查询到对应的用户信息
        user_id = token_data.get("data").get("user_id")
        # 根据用户id查询对应的账单数据
        user_bill_list = UserBase.query.get(user_id).bill_list
        print("查询到记录的数量={}".format(len(user_bill_list)))
    return jsonify(success=True, msg="test")


# 按照月份获取当月的全部账单信息
@bill_base.get("/list/<int:year>/<int:month>/")
def get_user_bill_by_month(year, month):
    # 获取给定月份的开始和结束的时间戳
    timestamp_list = get_start_and_end_timestamp_by_year_month(f"{year}-{month}", f"{year}-{month}")
    page = int(request.args.get("page", 1))
    page_size = int(request.args.get("page_size", 5))
    # 首先验证用户的token是否失效
    token = request.headers["Authorization"]
    if not token:
        # toekn为null，则表示用户没有登录，则无法获取基本信息
        return jsonify(success=False, msg="Token失效~")
    if len(timestamp_list) > 0:
        stamp_dict = timestamp_list[0]
        start_stamp = stamp_dict.get("start_timestamp")
        end_stamp = stamp_dict.get("end_timestamp")
        print(f"start_stamp={start_stamp} and end_stamp={end_stamp}")
        # 根据token获取用户的id
        token_data = JWTManager.verify_jwt(token)
        print("解析token得到的user_id={}".format(token_data))
        if token_data != "error":
            # 根据user_id查询到对应的用户信息
            user_id = token_data.get("data").get("user_id")
            pagination = BillDetail.query.filter(BillDetail.user_id == user_id).order_by(BillDetail.id.asc()).paginate(page=page,
                                                                                                          per_page=page_size,
                                                                                                          error_out=False)
            items = []
            for item in pagination.items:
                item_dict = {
                    'id': item.id,
                    'money_amount': item.money_amount,
                    'note': item.note,
                    'create_timestamp': item.create_timestamp,
                    'update_timestamp': item.update_timestamp,
                    'type_id': item.type_id,
                }
                items.append(item_dict)
            result = {
                'page': pagination.page,
                'per_page': pagination.per_page,
                'items': items,
                'total': pagination.total,
            }
            return jsonify(result)
        else:
            return jsonify(success=False, msg="Token失效~")
    else:
        return jsonify(success=False, msg="时间戳获取失败~")
