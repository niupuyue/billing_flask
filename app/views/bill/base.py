from flask import Blueprint, jsonify

bill_base = Blueprint('billBase', __name__, url_prefix='/bill')


# 获取用户基本信息
@bill_base.get('/list')
def get_user_info():
    return jsonify(success=True, msg="test")
