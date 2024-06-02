import socket

def client_program():
    host = '127.0.0.1'
    port = 5000

    client_socket = socket.socket()
    try:
        client_socket.connect((host, port))
    except socket.error as e:
        print(f"Connection failed. Error: {str(e)}")
        return

    message = input(" -> ")

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()

        print('Received from server: ' + data)

        message = input(" -> ")

    client_socket.close()

if __name__ == '__main__':
    client_program()
