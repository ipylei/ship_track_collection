# -*- coding: utf-8 -*-
import random
import re
import time

import logging
import requests

from lxml import etree

headers = {
    'Host': 'www.vesseltracker.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Cookie': 'SESSION=c8c37d9c-beaf-4397-b65e-4723dc95cb5b; _ga=GA1.2.1808695506.1564071913; _gid=GA1.2.552365655.1564071913',
    'Upgrade-Insecure-Requests': '1',
}

URL = 'https://www.vesseltracker.com/en/vessels.html?page={}&search={}'
XPATH = "//div[@class='results-table']//div[contains(@class,'row')]/div[contains(@class,'mmsi')]//text()"


def get_html(url):
    try:
        r = requests.get(url=url, timeout=100)
        if r.status_code == 200:
            print('当前url:{}请求成功'.format(url))
            html = r.content.decode()
            return html
    except:
        logging.error('当前url:{}请求失败，尝试重新请求'.format(url))
        html = get_html(url)
        return html


def parse_html(html):
    html = etree.HTML(html)
    mmsi_list = html.xpath(XPATH)
    return mmsi_list


if __name__ == '__main__':
    seq_list = 'CDEFGHIJKLMNOPQRSTUVWXYZ'
    for seq in seq_list:
        page = 1
        while True:
            url = URL.format(page, seq)
            html = get_html(url=url)
            if isinstance(html, str):
                mmsi_list = parse_html(html)
                if not mmsi_list:
                    break
                for mmsi in mmsi_list:
                    with open('./mmsi_category/mmsi_{}.txt'.format(seq), 'a+', encoding='utf-8') as f:
                        f.write(mmsi + '\n')
                page += 1
            else:
                break

    # # url = 'https://www.vesseltracker.com/en/vessels.html?page=188&search=A'
    # url = 'https://www.vesseltracker.com/en/vessels.html?page=20&search=B'
    # res = requests.get(url=url)
    # html = res.content.decode()
    # # print(html)
    # res = parse_html(html=html)
    # print(res)
