import socket

def server_program():
    host = '127.0.0.1'
    port = 5000

    server_socket = socket.socket()
    try:
        server_socket.bind((host, port))
    except socket.error as e:
        print(f"Bind failed. Error: {str(e)}")
        return

    server_socket.listen(2)
    print(f"Server listening on {host}:{port}")

    conn, address = server_socket.accept()
    print("Connection from: " + str(address))

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())

    conn.close()

if __name__ == '__main__':
    server_program()
