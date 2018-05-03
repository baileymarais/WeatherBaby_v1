#-*- coding:utf-8 -*-
"""
" Autho: BaileyMarais(maxun@live.cn)
" Date : 2018-05-03
"""

# import requests
# from bs4 import BeautifulSoup
# import pymysql
# import time
# from ip2Region import Ip2Region
from weather import weather

def main():
    worker = weather()
    worker.rebase()

    pass

    # db = pymysql.connect(host='aliyun.vps.ocx.cc', user='root', password='jc003j3mx', db='weatherbaby', use_unicode=True, charset="utf8")
    # cursor = db.cursor()
    # cursor.execute("select datasource_id,cityname,dataurl,id from citylist;")
    # data = cursor.fetchall()
    # for item in data:
    #     cursor.execute('select name from datasource where id={0}'.format(item[0]))
    #     datasource = cursor.fetchone()
    #     print("正在更新[{0}]在{1}上的数据...".format(item[1], datasource[0]))
    #     r = requests.get(item[2])
    #     if 200 == r.status_code:
    #         r.encoding = "utf-8"
    #         soup = BeautifulSoup(r.text, "html.parser")
    #         weatherlist = soup.find_all('li', class_=["sky skyid lv3 on", "sky skyid lv3", "sky skyid lv2 on", "sky skyid lv2"])
    #
    #         # 更新最近7天的天气
    #         if len(weatherlist) == 7:
    #             dayindex = 0
    #             for everyday in weatherlist:
    #                 if everyday.h1:
    #                     forecast_min = everyday.i.get_text().replace("℃","")
    #                     forecast_max = everyday.span.get_text().replace("℃","")
    #
    #                     localtime = time.localtime(time.time() + 86400 * dayindex)
    #                     sql = 'select id from weatherlist where forecast_date = "{0}" and citylist_id={1}'.format(
    #                         time.strftime("%Y-%m-%d", localtime),
    #                         item[3]
    #                     )
    #                     cursor.execute(sql)
    #                     forecast_id = cursor.fetchone()
    #                     if forecast_id and len(forecast_id) > 0:
    #                         # 这一天的数据存在，更新它
    #                         sql = 'update weatherlist set {0} {1} updated=now() where id={2}'.format(
    #                             "forecast_min=" + forecast_min + "," if len(forecast_min) > 0 else "",
    #                             "forecast_max=" + forecast_max + "," if len(forecast_max) > 0 else "",
    #                             forecast_id[0]
    #                         )
    #                     else:
    #                         sql = 'insert into weatherlist(forecast_date, forecast_min, forecast_max, updated, citylist_id) values("{0}",{1},{2},now(), {3});'.format(
    #                             time.strftime("%Y-%m-%d", localtime),
    #                             forecast_min if len(forecast_min) > 0 else "-1",
    #                             forecast_max if len(forecast_max) > 0 else "-1",
    #                             item[3]
    #                         )
    #
    #                     cursor.execute(sql)
    #                     dayindex += 1
    #
    #
    #             db.commit()
    #
    # db.close()

if __name__ == '__main__':
    main()
    # # r = requests.get('http://toy1.weather.com.cn/search?cityname=安岳')
    # # if 200 == r.status_code:
    # #     print(r.text)
    # # else:
    # #     print(r.status_code)
    # #
    # # print("finished!")
    # lib_ip = Ip2Region("ip2region.db")
    #
    # iplist = ["171.221.144.205", "47.94.85.143", "171.210.58.254", "182.131.10.11"]
    # for ip in iplist:
    #     print(ip + ":")
    #     btree = lib_ip.btreeSearch(ip)
    #     if isinstance(btree, dict):
    #         print(btree["region"].decode("utf-8").split('|')[3])
    #
    #     print("-------")