import socket

HOST = 'localhost'
PORT = 8080
BUFSIZ = 4096
ADDR = (HOST, PORT)

if __name__ == '__main__':
    
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(ADDR)
    data = input("Choose 'MAX' or 'MIN':")
    while True:
        if not data:
            break
        client_sock.send(str(data).encode('utf-8'))
        data = client_sock.recv(4096)
        print("Received from server: %s" %data.decode('utf-8'))
        if not data:
            break
        if data.decode('utf-8') == "Provide two numbers!":
            data_sent = input("Enter two number: ")
            #data_sent = "5 7"
            client_sock.send(str(data_sent).encode('utf-8'))
        # elif data.decode('utf-8') == "Wrong syntax":
        #     data = input("Choose 'MAX' or 'MIN': ")
        #     client_sock.send(data.encode('utf-8'))
    client_sock.close()