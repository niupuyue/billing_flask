from flask import Flask, Blueprint, jsonify

from app.utils.JWT import generate_token, verify_token
from app.views.bill import register_bill_views
from app.views.user import register_user_views
from app.views.util import register_util_views


def initialize_view(app: Flask):
    register_user_views(app)
    register_util_views(app)
    register_bill_views(app)

    # 默认的路由
    app.register_blueprint(Blueprint('index', __name__, url_prefix='/'))

    @app.route("/")
    def defalut_index():
        test_token = generate_token("123")
        print(test_token)
        test_user_id = verify_token(test_token)
        print(test_user_id)
        return jsonify(success=True, msg=test_user_id)
