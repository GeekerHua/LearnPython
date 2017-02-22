# coding=utf-8

import redis
#
# r = redis.StrictRedis(host='localhost', port=6379)
#
# # 写
# pipe = r.pipeline()
# pipe.set('apple', 'hello')
# pipe.execute()
#
# # 读取数据
# apple = r.get('apple')
#
# print(apple)


class RedisHelper():
    def __init__(self, host, port):
        self.__redis = redis.StrictRedis(host, port)

    def set(self, key, value):
        self.__redis.set(key, value)

    def get(self, key):
        return self.__redis.get(key)
