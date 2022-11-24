# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 22:25:09 2022

@author: ADMIN
"""

import socket
host = "127.0.0.1"
port = 9050

if __name__=="__main__":
    sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    r = input("nhap lenh ")
    sk.sendto(r.encode('utf-8'), (host,port))
    data, addr = sk.recvfrom(1024)
    print(data.decode('utf-8'))