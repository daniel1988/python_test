#!/usr/bin/python
# -*- coding: UTF-8 -*-
#encoding=utf-8
import MySQLdb

try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='root',db='formax_p2p',port=3306,charset="utf8")
    cursor=conn.cursor()
    cursor.execute('SET NAMES utf8')
    cursor.execute('select * from p2p_staff limit 1')
    data = cursor.fetchobj()

    # for v in data:
    #     print v

    print data[0:5]


    cursor.close()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])