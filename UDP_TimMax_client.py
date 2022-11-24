# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 16:11:56 2022

@author: ADMIN
"""

import socket
host = "127.0.0.1"
port = 9050

if __name__=="__main__":
    sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    s = input("nhap lenh ")
    sk.sendto(s.encode('utf-8'), (host,port))
    data,addr = sk.recvfrom(1024)
    print(data.decode('utf-8'))