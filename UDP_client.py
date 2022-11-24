# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 14:15:06 2022

@author: khai
"""
import socket
host = "127.0.0.1"
port = 9050

if __name__=="__main__":
    sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg = "hello"
    
    while True:
        msg = input()
        sk.sendto(msg.encode('utf-8'), (host, port))
        data, addr = sk.recvfrom(1024)
        if msg == "q":
            break
        print(data.decode('utf-8'))
        msg = "Nhan q de thoat"