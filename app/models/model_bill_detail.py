from datetime import datetime

from app.extensions.init_sqlalchemy import db


# 账单详情表
class BillDetail(db.Model):
    __tablename__ = 'bill_detail'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='用户ID')
    user_id = db.Column(db.Integer, db.ForeignKey('user_base.id'), nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('bill_type.id'), nullable=False)
    create_timestamp = db.Column(db.BigInteger, default=datetime.timestamp(datetime.now()))
    update_timestamp = db.Column(db.BigInteger, default=datetime.timestamp(datetime.now()),
                                 onupdate=datetime.timestamp(datetime.now()))
    enable = db.Column(db.Integer, default=1, comment='类型是否可用')
    money_amount = db.Column(db.Double, default=0.0, comment='账单金额')
    note = db.Column(db.String(255), nullable=True, comment='账单备注')
