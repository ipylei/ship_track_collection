# -*- coding: utf-8 -*-
import json
import re


def fiter_mmsi(file_name):
    with open(file_name + '.txt', 'r', encoding='utf-8') as f:
        mmsi_set = set()
        mmsi_list = f.readlines()
        for item in mmsi_list:
            mmsi = re.search('\d{9}', item.strip())
            if mmsi:
                mmsi_set.add(mmsi.group())
        with open(file_name + '.json', 'w', encoding='utf-8') as fb:
            json.dump(list(mmsi_set), fb)


def mmsi_count(file_name):
    with open(file_name + '.json') as f:
        mmsi_list = json.load(f)
        return len(mmsi_list)


if __name__ == '__main__':
    # string = '，369875000，'
    # mmsi = re.search('\d{9}', string.strip())
    # print(mmsi.group())

    # fiter_mmsi('JY_round')
    # fiter_mmsi('JY_other')

    # fiter_mmsi('MY_round')
    # fiter_mmsi('MY_other')

    # fiter_mmsi('total_mmsi')
    res = mmsi_count('total_mmsi')
    print(res)
    pass
