#-*- coding:utf-8 -*-
"""
" Autho: BaileyMarais(maxun@live.cn)
" Date : 2018-05-03
"""

# import requests
# from bs4 import BeautifulSoup
# import pymysql
# import time
from ip2Region import Ip2Region
from weather import weather
from socketserver import BaseRequestHandler, TCPServer
import conf


class WeatherService(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)

        lib_ip = Ip2Region("ip2region.db")
        btree = lib_ip.btreeSearch(self.client_address[0])
        if isinstance(btree, dict):
            print(btree["region"].decode("utf-8").split('|')[3])

        while True:
            msg = self.request.recv(conf.server_buffer_size)

            if not msg:
                break

            if msg == "exit();".encode("utf-8"):
                self.request.send("good bye".encode("utf-8"))
                break

            self.request.send(msg)

    def finish(self):
        print("Disconnect...", self.client_address)


if __name__ == '__main__':
    # w = weather()
    # cdtq = w.getweather("成都")
    # print(cdtq)
    #
    #
    serv = TCPServer((conf.server_listen_addr, conf.server_listen_port), WeatherService)
    serv.serve_forever()