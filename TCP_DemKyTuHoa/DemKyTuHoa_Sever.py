# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 11:44:50 2022

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
    
    while (True):
        print("Waiting for client")
        client, addr = sk.accept()
        print("Client address ",addr)
        # nhan du lieu
        print("Data for client %s " %client.recv(1024).decode('utf-8'))
        client.send("Hello client".encode('utf-8'))
        data = client.recv(1024)
        if not data:
            break
        so = data.decode('utf-8')
        count = 0
        for x in so:
            if x.isupper():
                count +=1
        data = str(count)
        client.send(data.encode('utf-8'))
        client.send(" bạn có muốn tiếp tục không?".encode('utf-8'))
        data = client.recv(1024)
        if data.decode('utf-8') == "no":
            break
        else:
            client.send("Mời bạn nhập tiếp: ".encode('utf-8'))
        client.close()
    sk.close()