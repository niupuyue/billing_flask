from apscheduler.jobstores import redis

from app import IYingConfig


class RedisDB():
    def __init__(self, host, port, passwd):
        # 建立数据库连接
        self.r = redis.Redis(host=host, port=port, password=passwd, decode_responses=True)

    def handle_redis_token(self, key, value=None):
        if value:
            # 如果value不是空，就设置key和value的值
            self.r.set(key, value)
        else:
            # 如果value为null，则直接从redis中取值
            redis_token = self.r.get(key)
            return redis_token


redis_db = RedisDB(IYingConfig.REDIS_HOST, IYingConfig.REDIS_PORT, IYingConfig.REDIS_PASSWD)
