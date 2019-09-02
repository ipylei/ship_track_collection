# -*- coding: utf-8 -*-
import time

# 伪造请求头
Headers = {
    'Host': 'www.shipxy.com',
    'Connection': 'keep-alive',
    # 'Content-Length': '14',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Origin': 'http://www.shipxy.com',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'http://www.shipxy.com/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Cookie': '_elane_maptype=MT_SEA; tc_TC=; _elane_shipfilter_length=0%2C40%2C41%2C80%2C81%2C120%2C121%2C160%2C161%2C240%2C241%2C320%2C321%2C9999; _elane_shipfilter_sog=0%2C1; _elane_shipfilter_country=0%2C1; _filter_flag=-1; tc_QX=; leadPageCookie=1; _elane_shipfilter_olength=0; _elane_shipfilter_type=%u8D27%u8239%2C%u96C6%u88C5%u7BB1%u8239%2C%u6CB9%u8F6E%2C%u5F15%u822A%u8239%2C%u62D6%u8F6E%2C%u62D6%u5F15%2C%u6E14%u8239%2C%u6355%u635E%2C%u5BA2%u8239%2C%u641C%u6551%u8239%2C%u6E2F%u53E3%u4F9B%u5E94%u8239%2C%u88C5%u6709%u9632%u6C61%u88C5%u7F6E%u548C%u8BBE%u5907%u7684%u8239%u8236%2C%u6267%u6CD5%u8247%2C%u5907%u7528-%u7528%u4E8E%u5F53%u5730%u8239%u8236%u7684%u4EFB%u52A1%u5206%u914D%2C%u5907%u7528-%u7528%u4E8E%u5F53%u5730%u8239%u8236%u7684%u4EFB%u52A1%u5206%u914D%2C%u533B%u7597%u8239%2C%u7B26%u540818%u53F7%u51B3%u8BAE%28Mob-83%29%u7684%u8239%u8236%2C%u62D6%u5F15%u5E76%u4E14%u8239%u957F%3E200m%u6216%u8239%u5BBD%3E25m%2C%u758F%u6D5A%u6216%u6C34%u4E0B%u4F5C%u4E1A%2C%u6F5C%u6C34%u4F5C%u4E1A%2C%u53C2%u4E0E%u519B%u4E8B%u884C%u52A8%2C%u5E06%u8239%u822A%u884C%2C%u5A31%u4E50%u8239%2C%u5730%u6548%u5E94%u8239%2C%u9AD8%u901F%u8239%2C%u5176%u4ED6%u7C7B%u578B%u7684%u8239%u8236%2C%u5176%u4ED6; Hm_lvt_adc1d4b64be85a31d37dd5e88526cc47=1563170810,1563286531,1563365757,1563681154; shipxy_v3_history_serch=s%u2606SHANGHAI%u2606477770800%u2606%u2606MMSI%uFF1A477770800%7Cs%u2606SHANGHAI%u2606111177777%u2606%u2606MMSI%uFF1A111177777%7Cs%u2606BRITISH%20WARSHIP%u2606233497888%u260635%u2606MMSI%uFF1A233497888%7Cs%u2606LIAONINGHAO886%u2606412769115%u260670%u2606MMSI%uFF1A412769115%7Cs%u2606LIAONINGHAO%u2606885201314%u260630%u2606MMSI%uFF1A885201314%7Cs%u2606CONSTANT%20FRIEND%20N83%u2606235004920%u260690%u2606MMSI%uFF1A235004920%7Cs%u2606MAGDALENA%u2606304682000%u260670%u2606MMSI%uFF1A304682000%7Cs%u2606CHANGBAISHAN99971%u2606622399971%u2606255%u2606MMSI%uFF1A622399971%7Cs%u2606CONSTANT%20FRIEND%20N83%u2606235004920%u260690%u2606IMO%uFF1A1; FD857C2AF68165D4=Dqzp+T6HZAFrvjX7G56MVkkF6vfRwjdkVOryEEZrkJ3kOnohGIgIKPhrrf+ERVrd5Tps9XJIRpA=; Hm_lvt_6d144245aa6f86a635b42289ce2d7502=1563681174,1563698321,1563718957,1563801029; .UserAuth2=8C8E090BEA22857494E84879A58851C6906783DFD62767BB86459F8926248666AD9030F6E4AA99152844EA72B8908267E9FCF54C5175BE2E3F1CD6A267A466E1F108ED09A91008D089089DF4AAE9F92A9B24753C37AA7A079A535C7D8B72CB3862BBA8F6CEE948EF91BA3AA48C6A87E3AE355F6846CB8F9710E90219DF97363C4E321068; Hm_lpvt_6d144245aa6f86a635b42289ce2d7502=1563804788; SERVERID=ce54c768aca7be22386d8a7ce24ecdae|1563808294|1563808286',

}

# 用户信息

# 账号1
# USERNAME = 'leiforver'
# PASSWORD = 'qq80231314'

# 账号2
# USERNAME = 'hello01'
# PASSWORD = 'qq201314'

# 账号3
# USERNAME = 'cxk007'
# PASSWORD = 'cxk245245'

# 账号4
USERNAME = 'mmlove'
PASSWORD = 'mm245245'

# USER_LIST = [('hello01', 'qq201314'), ('cxk007', 'cxk245245'), ('mmlove', 'mm245245'), ('leiforver', 'qq80231314')]
USER_LIST = [
    ('cxk007', 'cxk245245'),
    ('mmlove', 'mm245245'),
    ('leiforver', 'qq80231314'),
    ('hello01', 'qq201314')
]

# 是否自动登录
AUTO_LOGIN = 'true'
# AUTO_LOGIN = 'false'
# 登录地址
LOGIN_URL = 'http://www.shipxy.com/Home/Login'

# 船舶AIS数据接口
SHIP_INFO_API = 'http://www.shipxy.com/ship/GetShip'
Track_API = 'http://www.shipxy.com/Ship/GetTrack?shipid={}&btime={}&etime={}&enc=0'
HISTORY_VOYAGE_API = 'http://www.shipxy.com/Ship/GetHistoryVoyage'

# 周边国家
SURROUNDING_COUNTRIES = ['蒙古', '文莱', '不丹', '日本', '韩国', '朝鲜', '越南', '印度', '缅甸', '老挝', '菲律宾', '俄罗斯', '尼泊尔', '阿富汗',
                         '马来西亚', '印度尼西亚', '巴基斯坦', '哈萨克斯坦', '塔吉克斯坦', '吉尔吉斯斯坦']


def unix_time(dt):
    """时间格式转换为时间戳"""
    # 转换成时间数组
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    timestamp = str(int(time.mktime(timeArray)))
    return timestamp


def unix_time2(dt):
    """时间格式转换为时间戳"""
    # 转换成时间数组
    timeArray = time.strptime(dt, "%Y/%m/%d %H:%M")
    # 转换成时间戳
    timestamp = str(int(time.mktime(timeArray)))
    return timestamp


def format_date(unix_time):
    """时间戳转换为日期格式"""
    # 转换为时间数组
    timeArray = time.localtime(int(unix_time))
    # 转换为日期格式
    date = time.strftime("%Y%m%d_%H%M%S", timeArray)
    return date


START_TIME = unix_time('2019-8-5 0:0:0')
END_TIME = unix_time('2019-8-30 0:0:0')

if __name__ == '__main__':
    # result = unix_time('2019-07-23 11:47:02')
    # res = unix_time2('2019/7/1 0:0:0')

    # res = format_date(1561910400)
    # print(res)

    print(START_TIME)
    print(END_TIME)
    import random

    print(random.randint(3, 5))
    pass
