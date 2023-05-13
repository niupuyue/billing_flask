from flask import Blueprint, jsonify, request

from app.models import UserBase
from app.utils.JWT import JWTManager
from app.utils.time_utils import get_start_and_end_timestamp_by_year_month

bill_base = Blueprint('billBase', __name__, url_prefix='/bill')


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
    if len(timestamp_list) > 0:
        stamp_dict = timestamp_list[0]
        start_stamp = stamp_dict.get("start_timestamp")
        end_stamp = stamp_dict.get("end_timestamp")
        print(f"start_stamp={start_stamp} and end_stamp={end_stamp}")
    return jsonify(success=True, msg="test")
