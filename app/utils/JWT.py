# 生成token和验证token
from datetime import datetime, timedelta

import jwt

from app import IYingConfig


class JWTManager:
    @classmethod
    def generate_jwt_token(cls, user_id):
        """
        生成jwt
        :param user_id: 用户ID
        :return:
        """
        token = jwt.encode(
            {
                'exp': datetime.utcnow() + timedelta(seconds=IYingConfig.JWT_EXPIRE_DELTA_TIME),
                'iat': datetime.utcnow(),
                'data': {'user_id': user_id}
            },
            IYingConfig.SECRET_KEY, algorithm=IYingConfig.JWT_ALGORITHMS
        )

        return token

    @classmethod
    def verify_jwt(cls, token):
        """
        检验jwt
        :param token: jwt
        :return: dict: payload
        """
        try:
            payload = jwt.decode(token, IYingConfig.SECRET_KEY, algorithms=IYingConfig.JWT_ALGORITHMS)
        except jwt.PyJWTError as e:
            raise e

        return payload
