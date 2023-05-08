import os.path

from flask import Flask
from app.config import IYingConfig

# 设置Flask的配置信息
from app.extensions import initialize_plugs
from app.utils.script import initialize_script
from app.views import initialize_view


def create_app():
    app = Flask(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

    # 引入基本配置
    app.config.from_object(IYingConfig)

    # 注册插件
    initialize_plugs(app)

    # 注册路由
    initialize_view(app)

    # 注册初始化项目的命令
    initialize_script(app)

    # 判断已经在执行状态中
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        # 打印一下已启动的日志
        logo()

    return app


def logo():
    print('running~')
