from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions.init_sqlalchemy import db


class UserBase(db.Model, UserMixin):
    # 设置表名
    __tablename__ = 'user_base'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='用户ID')
    deviceid = db.Column(db.String(255), nullable=False, unique=True, comment='用户登录的deviceid，游客用户可使用该字段作为唯一标志')
    username = db.Column(db.String(20), comment='用户名')
    realname = db.Column(db.String(20), comment='真实名字')
    avatar = db.Column(db.String(255), comment='头像', default="/static/default/avatar.jpg")
    remark = db.Column(db.String(255), comment='备注')
    password_hash = db.Column(db.String(128), comment='哈希密码')
    enable = db.Column(db.Integer, default=0, comment='启用')
    create_at = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    update_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment='创建时间')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)
