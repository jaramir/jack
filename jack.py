#!/usr/bin/python

import socket
import os

s = socket.socket( socket.AF_UNIX )
s.connect( "/var/run/acpid.socket" )

commands = {
    "jack/headphone HEADPHONE plug": "nyxmms2 play",
    "jack/headphone HEADPHONE unplug": "nyxmms2 pause",
    }

buf = ""
while True:
    c = s.recv( 1 ).decode( "utf-8" )
    if c == "\n":
        print( "got event:", buf )
        if buf in commands:
            print( "executing command:", commands[buf] )
            os.system( commands[buf] )
        buf = ""
    else:
        buf += c
