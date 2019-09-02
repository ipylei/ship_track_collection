# -*- coding: utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler

'''
Python使用logging模块记录日志涉及四个主要类，使用官方文档中的概括最为合适：
    1>.logger提供了应用程序可以直接使用的接口；
    2>.handler将(logger创建的)日志记录发送到合适的目的输出；
    3>.filter提供了细度设备来决定输出哪条日志记录；
    4>.formatter决定日志记录的最终输出格式。
'''


# handler = logging.handlers.RotatingFileHandler(
#               'logs/myapp.log', maxBytes=100, backupCount=5)


def ship_logger():
    logging.basicConfig(level=logging.DEBUG)
    formater = logging.Formatter(
        # '%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # 自定义日志的输出格式，这个格式可以被文件输出流和屏幕输出流调用；
        '%(asctime)s - %(levelname)s - %(message)s')  # 自定义日志的输出格式，这个格式可以被文件输出流和屏幕输出流调用；

    logger_obj = logging.getLogger()

    fh1 = logging.handlers.RotatingFileHandler("日志_mmsi.txt", maxBytes=2516582400, backupCount=5)  # 300M
    # fh1 = logging.FileHandler("日志_mmsi.txt")  # 无效的mmsi
    fh1.setLevel(logging.INFO)

    fh2 = logging.FileHandler("日志_航次_航迹.txt")  # 没有航次
    fh2.setLevel(logging.WARNING)

    fh4 = logging.FileHandler("日志_请求.txt")  # 请求(AIS数据/航迹/轨迹)失败日志
    fh4.setLevel(logging.ERROR)

    fh5 = logging.FileHandler("日志_账号.txt")  # 返回status不是0的日志(表示该账号暂时可能无法使用)
    fh5.setLevel(logging.CRITICAL)  # 非常严重

    fh1.setFormatter(formater)  # 添加格式化输出，即调用我们上面所定义的格式，换句话说就是给这个handler选择一个格式；
    fh2.setFormatter(formater)  # 添加格式化输出，即调用我们上面所定义的格式，换句话说就是给这个handler选择一个格式；
    fh4.setFormatter(formater)  # 添加格式化输出，即调用我们上面所定义的格式，换句话说就是给这个handler选择一个格式；
    fh5.setFormatter(formater)  # 添加格式化输出，即调用我们上面所定义的格式，换句话说就是给这个handler选择一个格式；

    logger_obj.addHandler(fh1)  # logger对象可以创建多个文件输出流（fh）
    logger_obj.addHandler(fh2)  # logger对象可以创建多个文件输出流（fh）
    logger_obj.addHandler(fh4)  # logger对象可以创建多个文件输出流（fh）
    logger_obj.addHandler(fh5)  # logger对象可以创建多个文件输出流（fh）

    return logger_obj  # 将我们创建好的logger对象返回


ship_logger = ship_logger()

if __name__ == '__main__':
    # logger_obj.debug("debug message")  # 告警级别最低，只有在诊断问题时才有兴趣的详细信息。
    # logger_obj.info("info message")  # 告警级别比debug要高，确认事情按预期进行。

    # logger_obj.warning("warning message")  # 告警级别比info要高，该模式是默认的告警级别！预示着一些意想不到的事情发生，或在不久的将来出现一些问题（例如“磁盘空间低”）。该软件仍在正常工作。
    # logger_obj.error("error message")  # 告警级别要比warning要高，由于一个更严重的问题，该软件还不能执行某些功能。
    # logger_obj.critical("critical message")  # 告警级别要比error还要高，严重错误，表明程序本身可能无法继续运行。

    mmsi = '123456789'
    ship_logger.debug('请求mmsi:{}对应的(ais/航次/轨迹)信息时，请求失败'.format(mmsi))

    pass
