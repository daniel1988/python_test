#!/usr/bin/python
# -*- coding:utf8 -*-

import socket

cli = socket.socket()
host = socket.gethostname()
port = 9666

cli.connect((host, port))
print cli.recv(1024)
cli.close()