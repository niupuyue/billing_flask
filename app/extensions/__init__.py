from flask import Flask

from app.extensions.init_apscheduler import initialize_scheduler
from app.extensions.init_login import initialize_login
from app.extensions.init_migrate import initialize_migrate
from app.extensions.init_sqlalchemy import initialize_database
from app.extensions.init_upload import initialize_upload


def initialize_plugs(app: Flask) -> None:
    # 初始化数据库
    initialize_database(app)
    # 初始化定时任务
    initialize_scheduler(app)
    # 初始化上传文件
    # initialize_upload(app)
    # 初始化合并
    initialize_migrate(app)
    # 初始化登录模块
    initialize_login(app)
