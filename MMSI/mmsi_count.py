# -*- coding: utf-8 -*-


import os
import re
import json

# path = './Test'
# path = 'mmsi_A.txt'
# print(os.path.exists(path))  # 判断一个目录是否存在
# 2、os.makedirs(path) 多层创建目录
# 3、os.mkdir(path) 创建目录

# TODO A-Z的txt文件整合到一起
# file_list = os.listdir('../mmsi_category')
# for file in file_list:
#     with open('../mmsi_category/' + file, 'r', encoding='utf-8') as f:
#         mmsi_list = f.readlines()
#         for item in mmsi_list:
#             mmsi = re.search('\d{9}', item.strip())
#             if mmsi:
#                 mmsi.group()
#                 with open('total_mmsi.txt', 'a+', encoding='utf-8') as fb:
#                     fb.write(mmsi.group() + '\n')


# TODO 几个json文件的mmsi整合到一起
# all_mmsi_list = []
# # file_list = ['JY_other.json', 'JY_round.json']
# file_list = ['JY_other.json', 'JY_round.json', 'total_mmsi.json']
# for file in file_list:
#     with open(file, 'r', encoding='utf-8') as f:
#         file_mmsi_list = json.load(f)
#         print('文件:{},mmsi:{}条'.format(file, len(file_mmsi_list)))
#         all_mmsi_list.extend(file_mmsi_list)
#
# print('所有文件未去重，一共{}条'.format(len(all_mmsi_list)))
# all_mmsi_set = set(all_mmsi_list)
# all_filter_mmsi_list = list(all_mmsi_list)
# print('所有文件去重后，一共{}条'.format(len(all_mmsi_list)))
# with open('all_mmsi.json', 'w', encoding='utf-8') as f:
#     json.dump(all_filter_mmsi_list, f)


if __name__ == '__main__':
    with open('all_mmsi.json', 'r', encoding='utf-8') as fb:
        mmsi_list = json.load(fb)
        print(len(mmsi_list))
