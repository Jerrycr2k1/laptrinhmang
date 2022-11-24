# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 22:06:28 2022

@author: ADMIN
"""

host = '127.0.0.1'
port = 9050

import socket

if __name__=="__main__":
    sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sk.bind((host,port))
    
    print("watting client...")
    data,addr = sk.recvfrom(1024)
    print("client gui " + data.decode('utf-8'))
    str = data.decode('utf-8')
    s = str.split(' ')
    if s[0] == 'up':
        result = s[1].upper()
    else:
        result = s[1].lower()
    sk.sendto(result.encode('utf-8'),addr)
