#/usr/bin/env python
# -*- coding: UTF-8 -*-

def f(x):
    return x*x

print map(f, [1,3,5,7,9])

def f_1(x, y):
    return 10*x + y

print reduce(f_1, [1,2,3,4,5,6,7])


def fn(x, y):
    return x * 10 + y
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print reduce(fn, map(char2num, '13579'))


def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

print type('12342')
print type( str2int('12345') )


def uc_first(s):
    return s.capitalize()
name_list = ['adam', 'LISA', 'barT']


print map(uc_first, name_list)