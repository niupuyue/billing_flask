# 定义同事开启的处理请求的进程数量
import os
import multiprocessing

workers = 5
# 采用gevent库，支持异步处理请求，提高吞吐量
work_class = "gevent"
# 运行的地址和端口
bind = "0.0.0.0:8008"
chdir = os.path.dirname(os.path.abspath(__file__))
worker_class = 'sync'
timeout = 30

workers = multiprocessing.cpu_count() * 2 + 1
threads = 2
loglevel = 'info'
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'

# 运行gunicorn的命令
# app:表示需要运行的入口文件
# app:表示flask应用程序实例
# -c:表示的就是 --config，表示配置文件
# gunicorn app:app -c gunicorn.conf.py
# gunicorn -b 0.0.0.0:8008 app:app -c gunicorn.conf.py
# gunicorn -w 5 -b 0.0.0.0:8008 app:app -c gunicorn.conf.py

# 除此之外还可以设置其他的参数
# 生产环境不用这个配置项，但调试模式将其设置为True，并且可以看到在gunicorn启动时的所有配置项
debug = True

# 设置log日志文件，在执行之前先将这些文件创建好，否则会报错
# backlog = 2048
# pidfile = "log/gunicorn.pid"
# accesslog = "log/access.log"
# errorlog = "log/debug.log"

if not os.path.exists('logs'):
    os.mkdir('logs')

accesslog = os.path.join(chdir, "logs/gunicorn_access.log")
errorlog = os.path.join(chdir, "logs/gunicorn_error.log")
