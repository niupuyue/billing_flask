from flask import Flask
from flask_migrate import Migrate

from app.extensions.init_sqlalchemy import db

migrate = Migrate()


def initialize_migrate(app: Flask):
    migrate.init_app(app, db)
