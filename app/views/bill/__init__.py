from flask import Flask

from app.views.bill.base import bill_base


def register_bill_views(app: Flask):
    app.register_blueprint(bill_base)
