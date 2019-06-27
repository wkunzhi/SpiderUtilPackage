# -*- coding: utf-8 -*-
# __author__ = "zok"  362416272@qq.com
# Date: 2019-06-27  Python: 3.7

import redis
from DataMigration.config import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD


class RedisClient(object):
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT):
        if REDIS_PASSWORD:
            self._db = redis.Redis(host=host, port=port, password=REDIS_PASSWORD)
        else:
            self._db = redis.Redis(host=host, port=port)

    @property
    def db(self):
        return self._db


r = RedisClient().db
