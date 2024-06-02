import socket

def echo_client(host, port, message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.sendall(message.encode())
    received_data = client_socket.recv(1024)
    print("Received:", received_data.decode())
    client_socket.close()

if __name__ == "__main__":
    host = 'localhost'
    port = 12345
    message = "Hello, server!"
    echo_client(host, port, message)
