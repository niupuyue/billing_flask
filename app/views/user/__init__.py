from flask import Flask

from app.views.user.base import user_base


def register_user_views(app: Flask):
    app.register_blueprint(user_base)
