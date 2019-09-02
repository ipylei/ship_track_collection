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


# with open('JY_round.json', 'r', encoding='utf-8') as fb:
#     content = json.load(fb)
#     print(content)

if __name__ == '__main__':
    # fiter_mmsi('JY_round')
    # fiter_mmsi('JY_other')

    # fiter_mmsi('MY_round')
    # fiter_mmsi('MY_other')

    # string = '，369875000，'
    # mmsi = re.search('\d{9}', string.strip())
    # print(mmsi.group())
    pass
