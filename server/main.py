#-*- coding:utf-8 -*-
"""
" Autho: BaileyMarais(maxun@live.cn)
" Date : 2018-05-03
"""

# import requests
# from bs4 import BeautifulSoup
# import pymysql
import time
from ip2Region import Ip2Region
from weather import weather
from socketserver import BaseRequestHandler, TCPServer
import conf


weather_ = weather()
cached_cityname = {}


class WeatherService(BaseRequestHandler):
    def getcrc(self, text):
        ret = 0xFFFF
        for c in text:
            ret = ret ^ (ord(c) << 8)
            for n in range(0, 8):
                if ret & 0x8000:
                    ret = (ret << 1) ^ 0x1021
                else:
                    ret = ret << 1
            ret = ret & 0xFFFF

        return ret

    def handle(self):
        # 客户端上报消息格式(字符串区分大小写)：
        # --------------------------------------------
        # REQ|<PRODUCT>|<VERSION>|<DAYS>
        # PRODUCT: 产品名，目前只有WEATHERBABY
        # VERSION: 版本号
        # DAYS: 要获取的周期，最大是7天(含当天）
        # --------------------------------------------
        # REP|<TIMESTAMP>|<VERSION>|<PRODUCT>|<DAYS>|<DAY1>,[DAY2,[DAY3,[DAY4,[DAY(n)...]]]|<CRC>
        # TIMESTAMP: 服务器当前的时间戳
        # PRODUCT: 产品名，目前只有WEATHERBABY
        # DAY: 返回结果中包含的预测天数
        # DAY(n): 每一天的预测数据，多天数据用,分割，每一天内的数据用/分割，例如：
        #         DATE / MIN FORECAST / MAX FORECAST
        #         日期 / 预测最小温度   / 预测最大温度
        # CRC: 返回数据的CRC校验，校验值是返回内容中除了CRC本身以外所有字符的crc16，例如：
        #      REP|1525423688|1|WEATHERBABY|7|2018-05-04/17/25,2018-05-05/15/23,2018-05-06/15/27,2018-05-07/17/27,2018-05-08/16/24,2018-05-09/17/22,2018-05-10/17/21|14181

        lib_ip = Ip2Region("ip2region.db")
        btree = lib_ip.btreeSearch(self.client_address[0])
        if isinstance(btree, dict):
            cityname = btree["region"].decode(conf.default_charset).split('|')[3]

            if conf.mode_debug:
                cityname = "成都"

            if cached_cityname.get(cityname, None) == None:
                cached_cityname[cityname] = weather_.create_city(cityname)

        msg = self.request.recv(conf.server_buffer_size)
        if msg and len(msg) > 0:
            msgbuf = msg.decode(conf.default_charset).split('|')
            if len(msgbuf) == 4 and msgbuf[0] == "REQ" and msgbuf[1] == "WEATHERBABY" and msgbuf[2] == "1":
                request_days = int(msgbuf[3])
                retry = 0
                result = weather_.getweather(cityname, request_days)
                while (result == None or len(result) != request_days) and retry < 3:
                    weather_.rebase([cached_cityname[cityname]], request_days)
                    result = weather_.getweather(cityname, request_days)
                    retry += 1

                if result:
                    text_days = ""
                    for everyday in result:
                        text_days += everyday[0].strftime("%Y-%m-%d") + "/" + str(everyday[1]) + "/" + str(everyday[2]) + ","

                    text_days = text_days[0:len(text_days)-1]

                    rsp = "REP|" + str(int(time.time())) + "|1|WEATHERBABY|" + str(request_days) + "|" + text_days + "|"
                    rsp += str(self.getcrc(rsp))

                    if conf.mode_debug:
                        print(rsp)

                    self.request.send(rsp.encode(conf.default_charset))


if __name__ == '__main__':
    # w = weather()
    # cdtq = w.getweather("成都")
    # print(cdtq)
    #
    #

    serv = TCPServer((conf.server_listen_addr, conf.server_listen_port), WeatherService)
    serv.serve_forever()


    # s = "123456789"
    # print(hex(getcrc(s)))
