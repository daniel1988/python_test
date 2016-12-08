#!/usr/bin/python
# -*- coding:utf8 -*-
import argparse
import os,sys
import commands
# 需要守护启动的脚本
tasks=(
    "test_1.py",
    "test_2.py"
)

script_path = '/web/python_test/task_manager/'

parser = argparse.ArgumentParser(description="任务管理")

parser.add_argument('-s', action='store',
    dest='opt',
    default='start',
    help='启动所有脚本',
    choices=['start', 'restart', 'stop', 'status']
    )

args = parser.parse_args()



def service_start():
    for f in tasks:
        script = script_path + f
        ps = "ps -ef | grep " + f + " | grep -v grep | awk '{print $2}'"
        (status, output) = commands.getstatusoutput(ps)
        if output != '':
            print "%s \t\033[33;49;2m[ 运行中 ]\033[39;49;0m" % script
        else:
            command = "python " + script + ">/dev/null &"
            os.system(command)
            print "%s \t\033[32;49;2m[ 已启动 ]\033[39;49;0m" % script



def service_stop():
    for f in tasks:
        script = script_path + f
        ps = "ps -ef | grep " + script + " | grep -v grep | awk '{print $2}'"
        (status, output) = commands.getstatusoutput(ps)
        if output != '':
            command = "kill -9 %s" % output
            os.system(command)
            print "%s \t\033[31;49;2m[ 已停止 ] \033[39;49;0m" % script
        else:
            print "%s \t\033[37;49;2m[ 未运行 ]\033[39;49;0m" % script

def service_restart():
    service_stop()
    service_start()

def service_status():
    for f in tasks:
        script = script_path + f
        ps = "ps -ef | grep " + script + " | grep -v grep | awk '{print $2}'"
        (status, output) = commands.getstatusoutput(ps)
        if output != '':
            print "%s \t\033[33;49;2m[ 运行中 ]\033[39;49;0m" % script
        else:
            print "%s \t\033[37;49;2m[ 未运行 ]\033[39;49;0m" % script


def start():
    if args.opt == 'start':
        service_start()
    elif args.opt == 'stop':
        service_stop()
    elif args.opt == 'restart':
        service_restart()
    elif args.opt == 'status':
        service_status()
    else:
        service_status()

if __name__ == '__main__':
    start()
