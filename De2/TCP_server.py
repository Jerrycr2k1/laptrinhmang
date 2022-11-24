
import socket

HOST = 'localhost'
PORT = 8080
BUFSIZ = 4096
ADDR = (HOST, PORT)


def solve_data(str1, str2):
    lst = str2.split(" ")
    if str1 == 'max':
        return max(int(lst[0]), int(lst[1]))
    else:
        return min(int(lst[0]), int(lst[1]))
    

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(ADDR)
    server_socket.listen(5)
    server_socket.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    while True:
        print('Server waiting for connection...')
        client_sock, addr = server_socket.accept()
        print('Client connected from: ', addr)
        
        while True:
            data = client_sock.recv(BUFSIZ)
            if not data:
                break
            print("Received from client: %s" % data.decode('utf-8'))
            if data.decode('utf-8').lower() == 'max' or data.decode('utf-8').lower() == 'min':
                func = data.decode('utf-8').lower()
                notification = "Provide two numbers!"
                try:
                    client_sock.send(notification.encode('utf-8'))
                except KeyboardInterrupt:
                    print("Exited by user")
                
                data = client_sock.recv(BUFSIZ)
                data_sent = solve_data(func, data.decode('utf-8').strip())
                client_sock.send(str(data_sent).encode('utf-8'))
                break
            if data.decode('utf-8').lower() == 'end':
                notification = "Bye bye"
                try:
                    client_sock.send(notification.encode('utf-8'))
                    break
                except KeyboardInterrupt:
                    print("Exited by user")                                         
        client_sock.close()
    server_socket.close()