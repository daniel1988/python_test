#!/usr/bin/python
# -*- coding: UTF-8 -*-

fp = open('foo.log', 'ab')

print '文件名：', fp.name
print '访问模式:', fp.mode

# fp.write('this is a python file test\n')


fp = open('foo.log', 'r')
str = fp.read()
print str
print str.count('\n')