# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 11:30:14 2022

@author: BOSS
"""

import socket

if __name__ == "__main__":
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    host = 'localhost'
    post = 5050
    sk.connect((host, post))
    while True:
        sk.send("Hello sever".encode('utf-8'))
        data = input("Nhập chuỗi ký tự: ")
        sk.send(data.encode('utf-8'))
        
        data = sk.recv(1024)
        print("Data from sever: %s" % data.decode('utf-8'))
        data = sk.recv(1024)
        print("Data from sever: %s" % data.decode('utf-8'))
        data = input()
        sk.send(data.encode('utf-8'))
        if data == "no":
            break
    sk.close()