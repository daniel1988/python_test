#!/usr/bin/python
# -*- coding:utf-8 -*-
import time


print "%s%s" % (time.strftime("%Y%m%d%H%M%S", time.localtime()),".log")

print time.time()

print time.localtime(time.time())
print time.asctime( time.localtime(time.time()) )

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

print time.strptime("2016-08-11","%Y-%m-%d")
print time.mktime(time.strptime("2016-08-11","%Y-%m-%d"))

#calendar
import calendar
cal = calendar.month(2016,1)
print cal


import datetime
print datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")