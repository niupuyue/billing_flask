# 生成token和验证token
from datetime import datetime, timedelta

import jwt

from app.utils import Constants


def generate_token(user_id):
    """
    用户在一次绘画中生成的token，只要token不失效，就可以一直使用
    :param user_id: 用户id
    :return: 生成的token
    """
    # token_params 生成token的参数
    token_params = {
        'id': user_id,
        # exp：代表token的有效时间,datetime.utcnow():代表当前时间
        # timedelta:表示转化为毫秒
        'exp': datetime.utcnow() + timedelta(seconds=Constants.JWT_EXPIRE_SECOND)
    }
    # key:密钥,
    # algorithm:算法，算法是SHA-256
    # SHA-256:密码散列函数算法.256字节长的哈希值（32个长度的数组）---》16进制字符串表示，长度为64。信息摘要，不可以逆
    return jwt.encode(payload=token_params, key=Constants.SECRET_KEY, algorithm='HS256')


def verify_token(token_str):
    """
    验证当前token
    :param token_str:token字符串
    :return: 用户id
    """
    try:
        # 返回之前生成token的时候的字典，字典种包含id和exp
        user_data = jwt.decode(token_str, key=Constants.SECRET_KEY, algorithms='HS256')
        return user_data
    except Exception as ex:
        print(ex)
        return "error"
