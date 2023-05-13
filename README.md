# billing_flask

# 功能介绍


## 前端代码地址
1. Android https://github.com/niupuyue/Billing
2. 小程序(正在开发中...)
3. Flutter(正在开发中...)
4. H5(正在开发中...)
5. IOS(正在开发中...)

# 项目结构

# 使用方式

## Macos

### 开发环境
1. pycharm 2021.1.3
2. python 3.8
3. 下载并安装docker https://www.docker.com/

在项目根目录下运行
```angular2html
# 执行docker-compose.yml文件，此方法会在docker中生成一个名为billing_flask的容器，同时会创建相应的数据库
docker-compose up -d
# 执行完成之后，会创建mysql和redis的容器，可以通过docker ps查看
docker ps
# 执行flask相关命令
# 初始化flask需要使用到的数据库
flask db init
# 生成迁移脚本
flask db migrate
# 执行迁移脚本
flask db upgrade
# 此时已经帮我们创建好了数据库中的表
# 创建管理员用户
flask admin init
# 初始化 账单分类表 数据
flask admin init-type
```
在执行的过程中会发生如下错误：
```angular2html
Traceback (most recent call last):
  File "/Users/niupule/code/python_project/billing_flask/venv/lib/python3.9/site-packages/flask/cli.py", line 218, in locate_app
    __import__(module_name)
  File "/Users/niupule/code/python_project/billing_flask/app/__init__.py", line 7, in <module>
    from app.extensions import initialize_plugs
  File "/Users/niupule/code/python_project/billing_flask/app/extensions/__init__.py", line 7, in <module>
    from app.extensions.init_upload import initialize_upload
  File "/Users/niupule/code/python_project/billing_flask/app/extensions/init_upload.py", line 2, in <module>
    from flask_uploads import UploadSet, IMAGES, configure_uploads
  File "/Users/niupule/code/python_project/billing_flask/venv/lib/python3.9/site-packages/flask_uploads.py", line 26, in <module>
    from werkzeug import secure_filename, FileStorage
ImportError: cannot import name 'secure_filename' from 'werkzeug' (/Users/niupule/code/python_project/billing_flask/venv/lib/python3.9/site-packages/werkzeug/__init__.py)
```
这是由于flask中使用的werkzeug库导入包导致的错误，修改方式是，找打flask_uploads.py文件，将其中的
```python
from werkzeug import secure_filename, FileStorage
```
修改为
```python
# from werkzeug import secure_filename, FileStorage
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
```

直接运行启动文件即可
```python
python3 app.py
```

# 感谢
Flask项目灵感来源于 [pear-admin-flask](https://gitee.com/pear-admin/pear-admin-flask)
