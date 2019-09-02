# -*- coding: utf-8 -*-

import os
import json
import random
import time

import requests

from settings import *
from db import RedisClient
from python_exe_js import parse_ship_track
from loger import ship_logger


class Request:
    def __init__(self, request):
        self.request = request
        self.connet_count = 1

    def get(self, mmsi, **kwargs):
        if self.connet_count <= 5:
            try:
                return self.request.get(**kwargs)
            except Exception as E:
                ship_logger.error('当前第{}次请求MMSI:{}时，发生错误：{}'.format(self.connet_count, mmsi, E))
                self.connet_count += 1
                return self.get(mmsi, **kwargs)
        else:
            ship_logger.error('MMSI:{}已达到最大连接次数，准备放进二号队列'.format(mmsi))
            return

    def post(self, mmsi, **kwargs):
        if self.connet_count <= 5:
            try:
                return self.request.post(**kwargs)
            except Exception as E:
                ship_logger.error('当前第{}次请求MMSI:{}时，发生错误：{}'.format(self.connet_count, mmsi, E))
                self.connet_count += 1
                return self.post(mmsi, **kwargs)
        else:
            ship_logger.error('MMSI:{}已达到最大连接次数，准备放进二号队列'.format(mmsi))
            return


class SHIP:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.db = RedisClient()
        self.request = requests.Session()
        self.request.headers.update(Headers)

    def login(self, auto_login=AUTO_LOGIN):
        """
        :param username:
        :param password:
        :param auto_login: 下次是否自动登录
        :return:
        """
        data = {'username': self.username, 'password': self.password, 'autologin': auto_login}
        self.request.post(url=LOGIN_URL, data=data)
        self.request.get(url=LOGIN_URL)

    def get_ais_info(self, mmsi):
        """获取船舶AIS信息
        :param mmsi:
        :return: 返回船舶AIS信息(字典格式)
        """
        time.sleep(random.randint(3, 5))

        data = {'mmsi': mmsi}
        # r= self.request.post(url=SHIP_INFO_API,data=data)
        req = Request(request=self.request)  # 创建Request对象
        r = req.post(mmsi=mmsi, url=SHIP_INFO_API, data=data, timeout=60)
        if r:
            if r.status_code == 200:
                try:
                    ship_msg = json.loads(r.content.decode())
                    res_status = ship_msg.get('status')
                    ship_data = ship_msg.get('data')  # 列表套一个字典
                    if res_status == 0:  # todo 表示账号未封停
                        if ship_data:  # 表示能查询到该船舶
                            if isinstance(ship_data, list):
                                ship_info = ship_data[0]  # 取字典
                                return ship_info
                            elif isinstance(ship_data, dict):
                                return ship_data
                        else:
                            ship_logger.info('无效的MMSI:{}'.format(mmsi))
                    else:
                        ship_logger.critical('目前账号:{},获取MMSI:{}时，可能被封停或者Cookies已失效'.format(self.username, mmsi))
                        return '账号异常'
                except:
                    ship_logger.critical(
                        '当前账号:{},请求MMSI：{}对应的AIS数据失败，请求url：{},返回内容：{}'.format(self.username, mmsi, r.url,
                                                                              r.content.decode()))
                    self.db.push_mmsi(mmsi)
                    return '账号异常'
            else:
                ship_logger.error('请求MMSI:{}的AIS数据失败，返回状态码为:{}'.format(mmsi, r.status_code))
                self.db.push_mmsi(mmsi=mmsi)
        else:
            self.db.push_spare_mmsi(mmsi=mmsi)  # 放进二号队列

    def get_history_voyage(self, mmsi, start_time, end_time):
        """查询船舶历史航次信息
        :param mmsi:
        :param start_time:
        :param end_time:
        :return: 返回船舶历史航班信息(列表套字典，每个字典就是一个航次)
        """
        time.sleep(random.randint(3, 5))

        data = {'mmsi': mmsi, 'btime': start_time, 'etime': end_time}
        # r = self.request.post(url=HISTORY_VOYAGE_API, data=data)
        req = Request(request=self.request)  # 创建Request对象
        r = req.post(mmsi=mmsi, url=HISTORY_VOYAGE_API, data=data, timeout=60)
        if r:
            if r.status_code == 200:
                try:
                    content = json.loads(r.content.decode())
                    history_voyage = content.get('data')
                    if history_voyage:  # 表示有航次
                        return history_voyage
                    else:
                        ship_logger.warning('MMSI:{}暂无航次信息,放进2号队列'.format(mmsi))
                        self.db.push_spare_mmsi(mmsi=mmsi)
                except:
                    ship_logger.critical('当前账号:{},请求MMSI:{}对应的航次失败，请求url：{},返回内容：{}'.format(self.username, mmsi, r.url,
                                                                                            r.content.decode()))
                    self.db.push_mmsi(mmsi)
                    return '账号异常'
            else:
                ship_logger.error('请求MMSI:{}的航次信息失败，返回状态码为'.format(mmsi, r.status_code))
                self.db.push_mmsi(mmsi=mmsi)  # 再次放回去
        else:
            self.db.push_spare_mmsi(mmsi=mmsi)  # 放进二号队列

    def get_history_track(self, mmsi, start_time, end_time):
        """
        3.获取轨迹
        :param mmsi:
        :param start_time:
        :param end_time:
        :return: 返回船舶轨迹信息(列表套字典，每个字典都是一个航点)
        """
        time.sleep(random.randint(3, 5))

        track_url = Track_API.format(mmsi, start_time, end_time)
        # r = self.request.get(url=track_url)
        req = Request(request=self.request)  # 创建Request对象
        r = req.get(mmsi=mmsi, url=track_url, timeout=60)
        if r:
            if r.status_code == 200:
                try:
                    content = json.loads(r.content.decode())
                    ship_track = content.get('data')  # 加密格式的字符串
                    if ship_track:  # 表示有轨迹
                        ship_track_list = parse_ship_track(ship_track)  # 列表套字典
                        return ship_track_list
                    else:
                        ship_logger.warning('MMSI:{}在时间段{}-{}没有对应的轨迹信息'.format(mmsi, start_time, end_time))
                except:
                    ship_logger.critical('当前账号:{}，请求MMSI:{}对应的轨迹失败，请求url：{},返回内容：{}'.format(self.username, mmsi, r.url,
                                                                                            r.content.decode()))
                    self.db.push_mmsi(mmsi)
                    return '账号异常'
            else:
                ship_logger.error(
                    '请求MMSI:{}在时间段{}-{}对应的轨迹信息失败,返回状态码为,{}'.format(mmsi, start_time, end_time, r.status_code))
                self.db.push_mmsi(mmsi=mmsi)
        else:
            self.db.push_spare_mmsi(mmsi=mmsi)  # 放进二号队列

    def ship_type(self, type):
        """船舶类型"""
        if type in [35, 55]:
            ship_type = '军用'
        else:
            ship_type = '民用'
        return ship_type

    def voyage_area(self, country):
        """港口所属地区(我国，周边，其他)
        :param country:
        :return:
        """
        for area in SURROUNDING_COUNTRIES:
            if area in country:
                category = '中国周边'
                break
            elif '中国' in country:
                category = '中国'
                break
        else:
            category = '其他'
        return category

    def parse_voyage(self, voyage):
        """
        :param voyage:
        :return: 港口的国家或地区，本航次的开始计算时间，结束时间(离港时间)
        """
        port_country = voyage.get("PortCountry")
        btime = voyage.get("StartTime")
        etime = voyage.get("ATA")
        if btime and etime:
            return port_country, unix_time(btime), unix_time2(etime)

    def save_file(self, name, data):
        with open(name, 'w', encoding='utf-8') as f:
            json.dump(data, f)

    def collect_ship(self, mmsi):
        ship_ais_data = self.get_ais_info(mmsi)
        if ship_ais_data == '账号异常':
            return '账号异常'
        elif ship_ais_data:  # AIS数据
            ship_voyage_list = self.get_history_voyage(mmsi=mmsi, start_time=START_TIME, end_time=END_TIME)
            if ship_voyage_list == '账号异常':
                return '账号异常'
            elif ship_voyage_list:  # 航次列表
                for voyage in ship_voyage_list:
                    voyage_data = self.parse_voyage(voyage=voyage)
                    if voyage_data:  # 航次信息(单个航次所到达的：港口、开始时间、到港时间)
                        port_country, start_time, end_time = voyage_data

                        voyage_track = self.get_history_track(mmsi=mmsi, start_time=start_time, end_time=end_time)
                        if voyage_track == '账号异常':
                            return '账号异常'
                        elif voyage_track:  # 航次时间对应的每条航迹
                            type = ship_ais_data.get('type')  # 船舶类型
                            ship_type = self.ship_type(type=type)  # 类别(军用/民用)
                            port_area = self.voyage_area(port_country)  # 港口地区(我国/周边/其他)
                            path = '../{}/{}'.format(ship_type, port_area)  # 文件路径
                            if not os.path.exists(path):
                                os.makedirs(path)
                            # 构造文件名 mmsi_开始时间-结束时间
                            file_btime = format_date(start_time)
                            file_etime = format_date(end_time)
                            file_name = '{}_{}-{}'.format(mmsi, file_btime, file_etime)
                            file_path = '{}/{}.json'.format(path, file_name)
                            ship_data = {}
                            ship_data['ais_data'] = ship_ais_data  # AIS数据(字典格式)
                            ship_data['voyage'] = voyage  # 某一航次信息(字典格式)
                            ship_data['voyage_track'] = voyage_track
                            self.save_file(file_path, ship_data)
                            print('MMSI:{},类型:{}/{},文件名:{}保存成功'.format(mmsi, ship_type, port_area, file_name))

    def start(self):
        while True:
            mmsi = self.db.pop_mmsi()
            if mmsi:
                res = self.collect_ship(mmsi=mmsi)
                if res == '账号异常':
                    return
            else:
                return '已无mmsi'


def run():
    for user in USER_LIST:
        username, password = user
        ship = SHIP(username=username, password=password)
        ship.login()
        res = ship.start()
        if res == '已无mmsi':
            ship_logger.critical('该队列已无mmsi')
            return
    ship_logger.critical('目前所有账号都出现异常')


if __name__ == '__main__':
    run()

    # ship = SHIP(username=USERNAME, password=PASSWORD)
    # ship.login()

    # mmsi = '3038700001'  # 不存在的船舶mmsi
    # mmsi = '271040583'  # 有航次
    # mmsi = '304655000'  # 有航次
    # mmsi = '271040583'
    # mmsi = '369970347'  # 没有航次
    # mmsi ='229215000' # 有航次

    # start_time = '1561910400'
    # end_time = '1564070400'

    # 1.获取船舶信息
    # res = ship.get_ais_info(mmsi)
    # print(res)

    # 2.获取历史航次
    # res = ship.get_history_voyage(mmsi, START_TIME, END_TIME)
    # print(res)

    # 3.获取航迹
    # res = ship.get_history_track(mmsi, START_TIME, END_TIME)
    # print(res)

    # 4.解析每条航迹的开始时间、离港时间
    # voyage = {
    #     "Port": "",
    #     "StartPort": "阿姆巴利",
    #     "StartTime": "2019-07-02 12:14:31",
    #     "EndPort": "Zeytinburnu",
    #     "PortEn": "Zeytinburnu",
    #     "PortCountry": "土耳其",
    #     "ATA": "2019/7/11 0:52",
    #     "ATB": "",
    #     "ATD": "2019/7/12 16:44",
    #     "SailingHours": "204.6",
    #     "SailingDistance": "183.7",
    #     "SailingSpeed": "0.9"
    # }
    # res = ship.parse_voyage(voyage)
    # print(res)

    # 5.收集单个船舶
    # ship.collect_ship(mmsi)

    pass
