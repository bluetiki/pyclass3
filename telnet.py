#!/usr/bin/env python

import telnetlib
import time
import getpass
import socket
import sys

def telnet_connect(ip,port=23,timeout=10):
    try:
        telnet_conn = telnetlib.Telnet(ip,port,timeout)
    except socket.timeout:
        sys.exit('connection timed out')
    return telnet_conn

def login(telnet_conn,tries=3,timeout=10):
    user = input('Please enter your username: ')
    pw = getpass.getpass()
    output = telnet_conn.read_until(b"sername:",timeout).decode('utf-8', 'ignore')
    telnet_conn.write((user + '\n').encode('utf-8'))
    output += telnet_conn.read_until(b"assword:",timeout).decode('utf-8', 'ignore')
    telnet_conn.write((pw + '\n').encode('utf-8'))
    return output

def send_cmd(cmd,conn):
    conn.write((cmd + '\n').encode('utf-8'))
    time.sleep(1)
    out = conn.read_very_eager().decode('utf-8').splitlines(keepends=True)
    del out[0]
    del out[-1]
    return "".join(out)


def main():

    ip = input('Please input target IP Address: ')

    conn = telnet_connect(ip)
    login(conn)
    send_cmd('ter len 0',conn)
    out  = send_cmd('show ver',conn)
    print (out)

    conn.close()

if __name__ == "__main__":
    main()
