#!/usr/bin/env python3
#* coding: utf-8 *

def callbe(func):
    def wrapper(*args,**kw):
        print('begin call: %s' % func.__name__)
        func(*args,**kw)
        print ('end call: %s' % func.__name__)
    return wrapper

@callbe
def add_one(num):
    return num + 1


print(add_one(2))

