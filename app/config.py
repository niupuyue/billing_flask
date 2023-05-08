import logging
from urllib.parse import quote_plus as urlquote
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore


class IYingConfig:
    # 设置当前是否处于Debug状态
    DEBUG = True
    # 设置默认Host
    HOST = '127.0.0.1'
    # 设置默认端口
    PORT = 5555
    # 设置超级管理员
    SUPERADMIN = 'paulniu'
    # 设置系统的名称
    SYSTEM_NAME = "iying_billing"
    # 设置图片上传的位置
    UPLOADED_FILES_DEST = 'static/upload/'
    # 设置上传图片的类型
    UPLOADED_FILES_ALLOW = ['jpg', 'png', 'jpeg', 'webj', 'gif']
    UPLOADS_AUTOSERVE = True
    # 把对象序列化为 ASCII-encoded JSON 。如果禁用，那么 JSON 会被返回为一个 Unicode 字符串或者被 jsonify 编码为 UTF-8 格式。本变量应当保持 启用，因为在模块内把 JSON
    # 渲染到 JavaScript 时会安全一点
    JSON_AS_ASCII = False
    # 密钥用于会话 cookie 的安全签名，并可用于应用或者扩展的其他安全需求。本 变量应当是一个字节型长随机字符串，虽然 unicode 也是可以接受的
    SECRET_KEY = "iying-billing"
    # redis配置 HOST
    REDIS_HOST = '127.0.0.1'
    # redis配置 PORT
    REDIS_PORT = 6379
    # 配置MySql数据库 用户名
    MYSQL_USERNAME = "root"
    # 配置MySql数据库 密码
    MYSQL_PASSWORD = "123456"
    # 配置MySql数据库 HOST
    MYSQL_HOST = "127.0.0.1"
    # 配置MySql数据库 PORT
    MYSQL_PORT = 3306
    # 配置MySql数据库 名称
    MYSQL_DATABASE = "iYingBilling"
    # 设置MySql数据库的连接配置信息
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USERNAME}:{urlquote(MYSQL_PASSWORD)}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4"
    # 设置日志等级
    LOG_LEVEL = logging.WARN
    # 设置定时任务
    SCHEDULER_API_ENABLED = False
    # SCHEDULER_JOBSTORES指的就是作业存储器，我们把它存储到sqlite中
    SCHEDULER_JOBSTORES: dict = {
        'default': SQLAlchemyJobStore(
            url=f'mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}')
    }
    # SCHEDULER_EXECUTORS指的是执行器的配置，使用的类型是threadpool线程池，且设置最大线程数为20
    SCHEDULER_EXECUTORS: dict = {
        'default': ThreadPoolExecutor(20)
    }
    # SCHEDULER_JOB_DEFAULTS是任务的一些配置 coalesce指的是当由于某种原因导致某个任务积攒了好多次没有实际运行，如果coalesce为True，下次这个任务被执行时，只会执行1
    # 次，也就是最后这次，如果为False，那么会执行2次 max_instance就是说同一个任务同一时间最多有几个实例在跑
    SCHEDULER_JOB_DEFAULTS: dict = {
        'coalesce': False,
        'max_instances': 3
    }
