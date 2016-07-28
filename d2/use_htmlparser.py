#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()  #???????
        self._events = {}   #定义一个记录事件的dict
        self._counter = 0 # 记录条目数量
        self._tag = ''   #初始化self._tag
#在文本中查找对应的标签tag
    def handle_starttag(self, tag, attrs):
#如果有"<h3"开头的,且里面不为空,且有一个class单元,且class被赋值为"event-tile",后将所找到的命名为title,方便后续对应数据提取.
        if tag=='h3' and attrs and attrs[0][0] == 'class' and attrs[0][1] == 'event-title':
            self._tag = 'title'
        if tag=='time' and attrs and attrs[0][0] == 'datetime':
            self._tag = 'datetime'
        if tag=='span' and attrs and attrs[0][1] == 'event-location':
            self._tag = 'location'

    def handle_data(self, data):
        if self._tag == 'title':
            self._events[self._counter] = {'title':data}
        if self._tag == 'datetime':
            self._events[self._counter]['time'] = data
        if self._tag == 'location':
            self._events[self._counter]['location'] = data
            self._counter += 1
        self._tag = ''

    def printEvents(self):
        for k in self._events:
            # k表示字典里面的key，这里是纯数字即self._counter的值
            print('【title】:%s 【time】:%s 【location】:%s' % (self._events[k]['title'], self._events[k]['time'], self._events[k]['location']))

if __name__ == '__main__':
    with open('1.txt','r',encoding='UTF-8') as f:
        html_date=f.read()
    mParser = MyHTMLParser()
    mParser.feed(html_date)
    mParser.printEvents()
