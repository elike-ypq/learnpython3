#coding=utf-8

import requests
import re
from pprint import pprint


def get_stations():
    # 7@cqn|重庆南|CRW|chongqingnan|cqn|
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8968'
    r = requests.get(url,verify=False)
    patter = re.compile('([A-Z]+)\|([a-z]+)')
    items = dict(re.findall(patter,r.text))
    stations = dict(zip(items.values(),items.keys()))
    # for key in stations:
    #     print("{0}-->{1}".format(key,stations[key]))
    pprint(stations,indent=4)

if __name__ == '__main__':
    get_stations()
