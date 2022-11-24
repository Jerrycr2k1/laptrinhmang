
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 13:16:57 2022

@author: maidu
"""

# server gửi đi TCP

import socket
import sys

if __name__=='__main__':
    host = '127.0.0.1'
    port = 9050
    
    sk_server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    sk_server.bind((host,port))
    sk_server.listen(5)
    print("Đang kết nối tới client...")
    client , addr = sk_server.accept()
    # gửi đi hi
    client.send("Hi".encode('utf-8'))
    # nhận về hi
    data = client.recv(1024)
    print(data.decode())
    # gửi đi what
    client.send("What".encode('utf-8'))
    # Kiểm tra phép tính nhận về
    while True:
        check = client.recv(1024)
        temp = check.decode('utf-8')
        if(temp == '+' or temp == '-' or temp == '*' or temp == '/'):
            # nếu là phép tính thì gửi ok
            client.send("Ok".encode('utf-8'))
            # nhận lại 2 số
            str_val = client.recv(1024)
            str_val_temp = str_val.decode('utf-8').split(' ')
            
            if(temp == '+'):
                a = int(str_val_temp[0]) + int(str_val_temp[1])
                print(a)
            elif temp == '-':
                a = int(str_val_temp[0]) - int(str_val_temp[1])
                print(a)
            elif temp == '*':
                a = int(str_val_temp[0]) * int(str_val_temp[1])
                print(a)
            elif temp == '/':
                a = int(str_val_temp[0]) / int(str_val_temp[1])
                print(a)
            client.send(str(a).encode('utf-8'))
        else:
            sys.exit()
        client.send("Continue (Yes/No)?".encode('utf-8'))
        check_tiep = client.recv(1024)
        if(check_tiep.decode('utf-8') == 'No'):
            break
        
    sk_server.close()
        
    
    