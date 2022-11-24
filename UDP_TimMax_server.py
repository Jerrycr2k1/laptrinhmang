# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 12:02:44 2022

@author: ADMIN
"""

host = "127.0.0.1"
port = 9050
import socket 
if __name__=="__main__":
    sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sk.bind((host, port))
    print("doi client")
    data , addr = sk.recvfrom(1024)
    
    s = data.decode('utf-8')
    s = s.split(' ')
    res = max(s[0],s[1])
    sk.sendto(res.encode('utf-8'), addr)