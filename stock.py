#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import re
import datetime

def getStockInfo(url):
    """根据url获取信息"""
    stockList = []
    request = urllib2.Request(url)
    print request
    response = urllib2.urlopen(request)
    print response

    stockStr = response.read()
    stockList = stockStr.split(',')
    return stockList

def printStock(List):
    """打印相关信息"""
    print '***********price*****************' + List[1]
    print '***********float_price***********' + List[2]
    print '***********float_perct***********' + List[3] + '%'
    print '***********succ_unit*************' + List[4]+' shou'
    print '***********succ_price************' + List[5]

def getUrlByCode(code):
    """根据代码获取详细的url"""
    url = ''
    stockCode = ''
    if code == 'sh':
        url = 'http://hq.sinajs.cn/list=s_sh000001'
    elif code == 'sz':
        url = 'http://hq.sinajs.cn/list=s_sz399001'
    elif code == 'cyb':
        url = 'http://hq.sinajs.cn/list=s_sz399006'
    else:
        pattern = re.compile(r'^60*')
        match = pattern.match(code)
        if match:
            stockCode = 'sh'+ code
        else:
            stockCode = 'sz' + code
        url = 'http://hq.sinajs.cn/list=s_'+stockCode

    return url


#输入stock代码输出对应的价格信息
#code = raw_input('code: ')
codeDict = {
    'sh'     : 'shang hai zq',
    'sz'     : 'shen zheng zq',
    'cyb'    : 'chang ye ban',
    '601788' : 'guang da zheng quan',
    '000651' : 'ge li dian qi',
}

#http://hq.sinajs.cn/list=s_sh000001 (上海大盘查询)
#http://hq.sinajs.cn/list=s_sz399001 (深圳大盘查询)

count = 0;
while (count<=100):#循环100次后再退出
    # 循环字典
    for key in codeDict:
        print key + '--'+codeDict[key]

    code = raw_input('please select a code: ')
    now_time = datetime.datetime.now()

    #打印该code的信息
    url = getUrlByCode(code)
    stockInfo = getStockInfo(url)
    print stockInfo
    #print stockInfo
    # printStock(stockInfo)

    end_time = datetime.datetime.now()
    costTime =  (end_time - now_time).seconds
    print '总共花费时间'+str(costTime)+'秒'
    count +=1