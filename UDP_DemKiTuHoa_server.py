# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 22:46:37 2022

@author: ADMIN
"""
host = "127.0.0.1"
port = 9050
import socket 
if __name__=="__main__":
    sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sk.bind((host, port))
    
    print("doi client...")
    while(True):
        data, addr = sk.recvfrom(1024)
        if not data:
            break
        so = data.decode('utf-8')
        cnt = 0
        for x in so:
            if x.isupper():
                cnt = cnt + 1
        result = str(cnt)
        sk.sendto(result.encode('utf-8'), addr)
        
    
    
    
