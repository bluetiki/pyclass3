#!/usr/bin/env python

import telnetlib
import time


TELNET_PORT = 23
TELNET_TIMEOUT = 10

def connect(ip,user,pw):
    remote_conn = telnetlib.Telnet(ip,TELNET_PORT,TELNET_TIMEOUT)
    remote_conn.read_until(b"sername:",TELNET_TIMEOUT).decode('utf-8', 'ignore')
    remote_conn.write((user + '\n').encode('utf-8'))
    remote_conn.read_until(b"assword:",TELNET_TIMEOUT).decode('utf-8', 'ignore')
    remote_conn.write((pw + '\n').encode('utf-8'))
    time.sleep(1)
    remote_conn.read_very_eager().decode('utf-8')
    return remote_conn

def send_cmd(cmd,conn):
    conn.write((cmd + '\n').encode('utf-8'))
    time.sleep(1)
    output = conn.read_very_eager().decode('utf-8')
    return output


def main():

    ip_addr = '184.105.247.70'
    username = 'pyclass'
    password = '88newclass'

    conn = connect(ip_addr,username,password)
    
    send_cmd('ter len 0',conn)
    out  = send_cmd('show ver',conn)
    print (out)

    conn.close()

if __name__ == "__main__":
    main()
