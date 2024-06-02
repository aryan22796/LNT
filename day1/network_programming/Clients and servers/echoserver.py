# Let's consider a basic example of a client-server interaction using Python's socket programming:

# Server (Echo Server):

import socket

def echo_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Echo server is listening on port", port)

    while True:
        client_socket, client_address = server_socket.accept()
        print("Connection from:", client_address)

        data = client_socket.recv(1024)
        if data:
            client_socket.sendall(data)
        
        client_socket.close()

if __name__ == "__main__":
    host = 'localhost'
    port = 12345
    echo_server(host, port)
# netstat -an | findstr "12345"