#!/usr/bin/env python
# -*- coding: utf-8 -*-

import thread
import logging
from socketIO_client import SocketIO, LoggingNamespace
import sys 

reload(sys)
sys.setdefaultencoding('utf8')

logging.getLogger('requests').setLevel(logging.WARNING)
logging.basicConfig(level=logging.ERROR)

def on_response(*args):
    if type(args[0]) != str:
        print "\033[92m\033[1m" + args[0]["name"] + "\033[0m:", args[0]["text"]

with SocketIO('https://mede-chat-app.herokuapp.com/socket.io/', 443, LoggingNamespace) as socketIO:
    socketIO.emit('joinRoom', {
        "name": "Melih",
        "room": "deneme"
    })
    socketIO.on('message', on_response)
    thread.start_new_thread(socketIO.wait, ())
    while True:
        msg = raw_input() + "\n"
        socketIO.emit('message', {"name": "Melih", "text": msg})
        print "\033[A                             \033[A"

