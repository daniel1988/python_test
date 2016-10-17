#coding=utf-8
import urllib
import htmllib,formatter
import re
import datetime

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?[\.jpg|\.png|\.gif])" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    print imglist
    x = 0
    for imgurl in imglist:
        tmp_file = 'tmp/' + datetime.datetime.now().strftime("H%M%S%f") + '.jpg'
        urllib.urlretrieve(imgurl, tmp_file)
        x+=1

def getHref(html):
    reg = r'href="(http://.*?)"'
    link_re = re.compile(reg)
    link_list = re.findall(link_re, html)
    return link_list


def goAndGet(url):
    html = getHtml(url)
    getImg(html)
    link_list = getHref(html)
    for link in link_list:
        html = getHtml(link)
        getImg(html)


goAndGet("http://tieba.baidu.com/p/2460150866")