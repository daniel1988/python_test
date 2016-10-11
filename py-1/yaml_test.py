#!/usr/bin/python
# -*- coding: UTF-8 -*-
#加载yaml
import yaml

#读取文件
f = open('test.yaml')

#导入
x = yaml.load(f)

print x