#/usr/bin/python

# -*- coding:utf8 -*-


print map(lambda x:x*x, [1,2,3,4,5])


import random
import logging
logging.basicConfig(level=logging.INFO)
logging.info('random:%d' % random.randint(10,100))