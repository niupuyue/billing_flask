# 系统配置相关操作
from flask import Blueprint

util_blueprint = Blueprint('util', __name__, url_prefix='/utils')


@util_blueprint.get('/version_check')
def version_vercheck():
    return "hello"
