# 全局可能需要使用到的静态变量
import os

# 生成一个随机数
SECRET_KEY = os.urandom(16)
# TOKENT的有效时间
JWT_EXPIRE_SECOND = 24 * 60 * 60
