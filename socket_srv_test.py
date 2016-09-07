#!/usr/bin/python
# -*- coding:utf8 -*-

import socket

srv = socket.socket()
host = socket.gethostname()
port = 9666
srv.bind((host, port))
srv.listen(5)

while True:
    c, addr = srv.accept()
    print 'Remote Addr:', addr
    c.send('Hello World,')
    c.close()