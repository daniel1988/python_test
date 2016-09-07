#!/usr/bin/python
# -*- coding:utf-8 -*-


def multiplicationTable():
    # i = 1
    # while( i <= 9 ):
    #     j = 1
    #     while ( j <= i ):
    #         print i , '*' , j ,'=',i*j,
    #         j += 1
    #     print
    #     i += 1

    for i in range(1,10):
        for j in range(1,i+1):
            print i, '*', j, '=', i*j,
        print

def main():
    multiplicationTable()


main()