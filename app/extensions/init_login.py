from flask import Flask
from flask_login import LoginManager

from app.models.model_user import UserBase


def initialize_login(app: Flask):
    login_manager = LoginManager()
    login_manager.init_app(app)

    login_manager.login_view = 'user.base.login'
    login_manager.login_message = u'请登录以访问此页面'

    @login_manager.user_loader
    def load_user(user_id):
        user = UserBase.query.get(int(user_id))
        return user
