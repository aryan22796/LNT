import socket

def daytime_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    data = client_socket.recv(1024)
    print("Received:", data.decode('ascii'))
    client_socket.close()

if __name__ == "__main__":
    host = 'localhost'  # Use '127.0.0.1' if on the same machine
    port = 12345
    
    daytime_client(host, port)
