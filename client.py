# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 14:32:56 2022

@author: vuphu
"""
#client
import socket

if __name__=='__main__':
    host = '127.0.0.1'
    port = 9050
    
    sk_client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    sk_client.connect((host,port))
    # gửi đi hi cho server
    sk_client.send("Hi".encode('utf-8'))
    # nhận về hi
    data = sk_client.recv(1024)
    print(data.decode('utf-8'))
    # nhận về what
    data_1 = sk_client.recv(1024)
    print(data_1.decode('utf-8'))
    while True:
        # gửi phép tính tới server
        op = input("Nhập phép tính: ")
        sk_client.send(op.encode('utf-8'))
        # nếu nhận ok thì gửi lại cho server 2 số a và b
        check_ok= sk_client.recv(1024)
        print(check_ok)
        if(check_ok.decode('utf-8') == 'Ok'):
            val_a_b = "5 2"
            sk_client.send(val_a_b.encode('utf-8'))
            # sau khi gửi đi 2 số thì nhận lại kết quả
            res = sk_client.recv(1024)
            print(res.decode('utf-8'))
            conti = sk_client.recv(1024)
            print(conti.decode('utf-8'))
            tiep = input("Yes or No? : ")
            sk_client.send(tiep.encode('utf-8'))
            if(tiep == "No"):
                break
    sk_client.close()
    
    