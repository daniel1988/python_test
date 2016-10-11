#!/usr/bin/env python

import sys, glob, os, socket

thrift_dir = os.getcwd() + "/Thrift"
sys.path.append(thrift_dir)
from HelloService import HelloService
from HelloService.ttypes import *


from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class HelloWorldHandler:
  def __init__(self):
    self.log = {}

  def ping(self):
    print "ping()"

  def sayHello(self):
    print "sayHello()"
    return "say hello from " + socket.gethostbyname(socket.gethostname())

  def sayMsg(self, msg):
    print "sayMsg(" + msg + ")"
    return "say " + msg + " from " + socket.gethostbyname(socket.gethostname())

handler = HelloWorldHandler()
processor = HelloService.Processor(handler)
transport = TSocket.TServerSocket(port=9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

# You could do one of these for a multithreaded server
#server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
#server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)

print 'Starting the server...'
server.serve()
print 'done.'