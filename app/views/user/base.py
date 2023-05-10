from flask import Blueprint, jsonify

user_base = Blueprint('userBase', __name__, url_prefix='/user')


# 获取用户基本信息
@user_base.get('/info/')
def get_user_info():
    return jsonify(success=True, msg="test")
