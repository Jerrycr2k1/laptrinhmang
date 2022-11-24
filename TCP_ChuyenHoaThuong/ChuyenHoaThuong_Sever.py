# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 12:24:06 2022

@author: BOSS
"""

import socket

if __name__ == "__main__":
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    host = 'localhost'
    post = 5050
    sk.bind((host,post))
    sk.listen(5)
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    print("Waiting for client")
    client, addr = sk.accept()
    print("Client address ",addr)
    # nhan du lieu
    print("Data for client %s " %client.recv(1024).decode('utf-8'))
    client.send("Hello client".encode('utf-8'))
    data = client.recv(1024)
    
    so = data.decode('utf-8')
    s = so.split(",")
    if s[0] == "UP":
        data = s[1].upper()
    else:
        data = s[1].lower()
        
    client.send(data.encode('utf-8'))
    client.close()
    
    sk.close()