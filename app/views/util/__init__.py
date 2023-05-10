from flask import Flask

from app.views.util.base import util_blueprint


def register_util_views(app: Flask):
    app.register_blueprint(util_blueprint)
