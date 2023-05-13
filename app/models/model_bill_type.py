from datetime import datetime

from app.extensions.init_sqlalchemy import db


# 账单类型(基础)
class BillType(db.Model):
    # 设置表名
    __tablename__ = 'bill_type'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='账单类型名称')
    type_name = db.Column(db.String(128), nullable=False, unique=True, comment='账单类型的名称')
    type_icon = db.Column(db.String(255), nullable=False, unique=True, comment='账单icon')
    enable = db.Column(db.Integer, default=1, comment='类型是否可用')
    create_timestamp = db.Column(db.BigInteger, default=datetime.timestamp(datetime.now()))
    update_timestamp = db.Column(db.BigInteger, default=datetime.timestamp(datetime.now()),
                                 onupdate=datetime.timestamp(datetime.now()))
