import datetime

from app.extensions.init_sqlalchemy import db


class VersionModel(db.Model):
    __tablename__ = 'app_version'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='版本号的ID')
    create_at = db.Column(db.DateTime, default=datetime.datetime.now, comment='创建时间')
    update_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment='创建时间')
    platform = db.Column(db.Integer, default=0, comment='版本的平台 0:web,1:weiChat,2:Android,3:IOS')
    version_name = db.Column(db.String(20), default='000.000.000', comment='对应的版本号')
    enable = db.Column(db.Integer, default=0, comment='启用')
