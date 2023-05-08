from flask import Flask, Blueprint, jsonify

from app.views.bill import register_bill_views
from app.views.user import register_user_views
from app.views.util import register_util_views


def initialize_view(app: Flask):
    register_user_views(app)
    # register_util_views(app)
    register_bill_views(app)

    # 默认的路由
    app.register_blueprint(Blueprint('index', __name__, url_prefix='/'))

    @app.route("/")
    def defalut_index():
        return jsonify(success=True, msg="测试页面首页")

    # 系统配置相关操作
    util_blueprint = Blueprint('util', __name__, url_prefix='/utils')

    @util_blueprint.get('/version_check')
    def version_vercheck():
        return ""
