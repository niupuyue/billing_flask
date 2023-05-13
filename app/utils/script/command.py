import datetime
import os

import click
from flask.cli import AppGroup

from app.extensions.init_sqlalchemy import db
from app.models.model_user import UserBase
from app.utils.script.newmodular.new import NewViewModular

BaseCommand = AppGroup("admin")

# 当前时间
now_time = datetime.datetime.now()
userdata = [
    UserBase(
        username='admin',
        deviceid='123456',
        password_hash='pbkdf2:sha256:150000$raM7mDSr$58fe069c3eac01531fc8af85e6fc200655dd2588090530084d182e6ec9d52c85',
        create_at=now_time,
        enable=1,
        realname='超级管理',
        remark='要是不能把握时机，就要终身蹭蹬，一事无成！',
        avatar='http://127.0.0.1:5000/_uploads/photos/1617291580000.jpg',
    )
]


# 初始化数据库
@BaseCommand.command("init")
def init_db():
    # 加载系统必须的用户数据
    db.session.add_all(userdata)
    print("加载系统必须用户数据成功")
    db.session.commit()
    print("基础数据存入")


# 创建一个新的用户
@BaseCommand.command("user")
def add_normal_user():
    user_base = UserBase(
        username='admin',
        deviceid='1234567',
        password_hash='pbkdf2:sha256:150000$raM7mDSr$58fe069c3eac01531fc8af85e6fc200655dd2588090530084d182e6ec9d52c85',
        create_at=now_time,
        create_timestamp=datetime.datetime.timestamp(now_time),
        enable=1,
        realname='超级管理',
        remark='要是不能把握时机，就要终身蹭蹬，一事无成！',
        avatar='http://127.0.0.1:5000/_uploads/photos/1617291580000.jpg',
    )
    db.session.add(user_base)
    db.session.commit()


@BaseCommand.command()
@click.option('--type', prompt="请输入类型", help='新增的类型')
@click.option('--name', prompt="请输入新增的名称", help='新增的名称')
def new(type, name):
    if type == 'view':
        if name.count('/') > 1:
            print("目前只支持二级目录，多级目录需要蓝图嵌套，本命令暂不支持，请手动创建")
            quit()
        if type == "view" and os.path.exists(f"applications/view/{name}.py"):
            print(f'已经存在视图模块{name}.py')
            quit()
        NewViewModular(name=name).new_view()
