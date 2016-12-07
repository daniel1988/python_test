#!/usr/bin/python
# -*- coding:utf8 -*-

# 生成一个列表
l = [x*x for x in range(10)]
print l

print [m + n for m in 'ABC' for n in 'XYZ']
L = ['Hello', 'World', 'Apple']
print [s.lower() for s in L]

# # 生成器
# g = (x*x for x in range(10))
# print g
# print g.next()
# for x in g:
#     print x

# yeild
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1

# g = fib(6)
# print g.next()
# print g.next()
# print g.next()
# print g.next()

for n in fib(6):
    print n