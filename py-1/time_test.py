#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
import datetime


# print "%s%s" % (time.strftime("%Y%m%d%H%M%S", time.localtime()),".log")

# print time.time()

# print time.localtime(time.time())
# print time.asctime( time.localtime(time.time()) )

# print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# print time.strptime("2016-08-11","%Y-%m-%d")
# print time.mktime(time.strptime("2016-08-11","%Y-%m-%d"))

# #calendar
# import calendar
# cal = calendar.month(2016,1)
# print cal


# import datetime
# print datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")



now = time.time()

today = datetime.date.today() + datetime.timedelta(1)
print today

tomorrow = time.mktime(today.timetuple())

print int(tomorrow - now)

print datetime.datetime.now()

print int( time.mktime(today.timetuple()) - time.time() )

expire_day = datetime.date.today() + datetime.timedelta(days=7)

print expire_day
print int( time.mktime(expire_day.timetuple()) )
