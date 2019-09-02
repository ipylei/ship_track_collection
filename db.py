# -*- coding: utf-8 -*-
import json

import redis

# redis数据库配置
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_KEY = 'mmsi'  # 一共42676
SPARE_KEY = 'mmsi2'  # 备用列表，存储暂无航次的mmsi


class RedisClient:
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, redis_db=REDIS_DB):
        self.db = redis.StrictRedis(host=host, port=port, db=redis_db)

    def push_mmsi(self, mmsi, key=REDIS_KEY):
        self.db.lpush(key, mmsi)

    def pop_mmsi(self, key=REDIS_KEY):
        mmsi = self.db.rpop(key)
        if mmsi:
            return mmsi.decode('utf-8')

    def count_mmsi(self, key=REDIS_KEY):
        return self.db.llen(key)

    def show_all_mmsi(self, key=REDIS_KEY):
        mmsi_list = []
        all_mmsi = self.db.lrange(key, 0, -1)
        if all_mmsi:
            for mmsi in all_mmsi:
                mmsi_list.append(mmsi.decode('utf-8'))
            return mmsi_list

    def push_spare_mmsi(self, mmsi, spare_key=SPARE_KEY):
        self.db.lpush(spare_key, mmsi)


def get_all_mmsi():
    with open('MMSI/all_mmsi.json', 'r', encoding='utf-8')  as f:
        mmsi_list = json.load(f)
        return mmsi_list


def push_all_to_key():
    db_client = RedisClient()
    mmsi_list = get_all_mmsi()
    # print(len(mmsi_list))
    for mmsi in mmsi_list:
        db_client.push_mmsi(mmsi=mmsi)


def pop_key2_to_key():
    db_client = RedisClient()
    # spare_list = db_client.show_all_mmsi(key=SPARE_KEY)
    while True:
        mmsi = db_client.pop_mmsi(key=SPARE_KEY)
        if mmsi:
            db_client.push_mmsi(mmsi=mmsi)
        else:
            return


if __name__ == '__main__':
    # db_client = RedisClient()
    # count = db_client.count_mmsi()
    # print(count)

    # push_all_to_key()  # 把all_mmsi.json中的mmsi推送到REDIS_KEY中
    pop_key2_to_key()  # 把备用的SPARE_KEY中的mmsi推到REDIS_KEY中
    pass
