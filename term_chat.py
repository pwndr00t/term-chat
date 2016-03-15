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

data = ""

def on_response(*args):
    if type(args[0]) != str:
        data = True
        print "\033[92m\033[1m" + args[0]["name"] + "\033[0m:", args[0]["text"]
    else:
        data = False

with SocketIO('https://mede-chat-app.herokuapp.com/socket.io/', 443, LoggingNamespace) as socketIO:
    user = raw_input("Enter your chat name please: ")
    socketIO.emit('joinRoom', {
        "name": user,
        "room": "deneme"
    })
    socketIO.on('message', on_response)
    thread.start_new_thread(socketIO.wait, ())
    while True:
        msg = raw_input()
        #TODO: @Melih This if is necessary or can we solve this from server side? We need sth. like
        # When user on state 'typing' and a new message reached, then put received message first
        # and regenerate raw_input box with previous state.
        if data:
            print msg, raw_input()
        else:
            print ""
            socketIO.emit('message', {"name": "\033[92m\033[1m\n" + user, "text": msg})
            print "\033[A                             \033[A"
