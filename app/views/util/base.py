# 系统配置相关操作

from flask import Blueprint, jsonify

from app.models import BillType

util_blueprint = Blueprint('util', __name__, url_prefix='/utils')


@util_blueprint.get('/version_check/')
def version_vercheck():
    return "hello"


@util_blueprint.get('/bill_type/test/')
def get_bill_type_test():
    """
    获取所有账单分类信息数据
    :return:
    """
    pagination = BillType.query.filter(BillType.enable == 1).order_by(BillType.id.asc()).paginate(page=1, per_page=5,
                                                                                                  error_out=False)
    items = []
    for item in pagination.items:
        item_dict = {
            'id': item.id,
            'type_name': item.type_name,
            'type_icon': item.type_icon
        }
        items.append(item_dict)
    result = {
        'page': pagination.page,
        'per_page': pagination.per_page,
        'items': items,
    }
    return jsonify(result)


@util_blueprint.get('/bill_type/')
def get_bill_type():
    """
    获取所有账单分类信息数据
    :return:
    """
    pagination = BillType.query.filter(BillType.enable == 1).order_by(BillType.id.asc())
    items = []
    for item in pagination:
        item_dict = {
            'id': item.id,
            'type_name': item.type_name,
            'type_icon': item.type_icon
        }
        items.append(item_dict)
    result = {
        'items': items,
    }
    return jsonify(result)
