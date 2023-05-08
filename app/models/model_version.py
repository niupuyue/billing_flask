import datetime

from app.extensions.init_sqlalchemy import db


class VersionModel(db.Model):
    __tablename__ = 'app_version'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='版本号的ID')
    create_at = db.Column(db.DateTime, default=datetime.datetime.now, comment='创建时间')
    update_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment='创建时间')
