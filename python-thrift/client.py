#!/usr/bin/env python

import sys, glob, os

thrift_dir = os.getcwd() + "/Thrift"
sys.path.append(thrift_dir)
from HelloService import HelloService
from HelloService.ttypes import *
from HelloService.constants import *



from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
  # Make socket
  transport = TSocket.TSocket('127.0.0.1', 9090)

  # Buffering is critical. Raw sockets are very slow
  transport = TTransport.TBufferedTransport(transport)

  # Wrap in a protocol
  protocol = TBinaryProtocol.TBinaryProtocol(transport)

  # Create a client to use the protocol encoder
  client = HelloService.Client(protocol)

  # Connect!
  transport.open()

  client.ping()
  print "ping()"

  msg = client.sayHello()
  print msg
  msg = client.sayMsg(HELLO_IN_KOREAN)
  print msg

  transport.close()

except Thrift.TException, tx:
  print "%s" % (tx.message)
