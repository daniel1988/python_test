# -*- coding: utf-8 -*-
from socket import *
from time import ctime

# Address and Port
HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

# BuffSize
BUFSIZ = 1024

# build socket
tcpSerSock = socket(AF_INET, SOCK_STREAM)
# bind socket
tcpSerSock.bind(ADDR)
# listen 5 client
tcpSerSock.listen(5)

try:
    while True:
        print 'waiting for connection...'
        # build client socket
        tcpCliSock, addr = tcpSerSock.accept()
        print '...connect from:', addr

        # accept data and process
        while True:
            data = tcpCliSock.recv(BUFSIZ)
            print data
            if not data:
                break
            tcpCliSock.send('[%s] %s' % (ctime(), data))

            # close client socket
            # tcpCliSock.close()
except EOFError, KeyboardInterrupt:
    tcpSerSock.close()