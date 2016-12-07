#/usr/bin/python

# -*- coding:utf8 -*-

l = [5,23,23,34,1]
print sorted(l)

def desc(x,y):
    if x > y:
        return -1
    else:
        return 1
print sorted(l, desc)