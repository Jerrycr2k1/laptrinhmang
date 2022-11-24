# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 10:47:20 2022

@author: ADMIN
"""
host = "127.0.0.1"
port = 9050
import socket 
if __name__=="__main__":
    sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while(True):
        msg = input("nhap chuoi : ")
        if(msg == ""):
            break
        sk.sendto(msg.encode('utf-8'), (host,port))
        data, addr = sk.recvfrom(1024)
        print(data.decode('utf-8'))
    
