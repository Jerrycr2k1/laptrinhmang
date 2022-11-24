# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 12:51:19 2022

@author: BOSS
"""

import socket

if __name__ == "__main__":
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    host = 'localhost'
    post = 5050
    while True:
        r = input("Nhập 'r' để connect!")
        if(r == 'r'):
            break
        
    sk.connect((host, post))
    sk.send("Hello sever".encode('utf-8'))
    
    data = sk.recv(1024)
    print("Data from sever: %s" % data.decode('utf-8'))
    
    data = input("Nhập otp, a, b, a:  ")
    sk.send(data.encode('utf-8'))
    
    data = sk.recv(1024)
    print("Data from sever: %s" % data.decode('utf-8'))
    
    sk.close()