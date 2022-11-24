# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 13:46:17 2022

@author: khai
"""

import socket
if __name__=="__main__":
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    host = 'localhost'
    port = 5050
    sk.bind((host, port))
    sk.listen(5)
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    while(True):
        print("waiting for client")
        client,  addr = sk.accept()
        print("Client address ", addr)
        #nhan du lieu
        
        data = client.recv(1024) 
        f = open(data.decode('utf-8'), 'wb')
        data = client.recv(1024) 
        if not data:
            break
        f.write(data)
        f.close()
        client.send("Da nhan".encode('utf-8'))
        break
        client.close()
    sk.close()