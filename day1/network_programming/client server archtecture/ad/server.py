import socket
import threading

# A simple key-value store
store = {}

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    with conn:
        while True:
            # Step 4: Receiving Requests
            data = conn.recv(1024)
            if not data:
                break
            
            request = data.decode().strip().split()
            if len(request) < 1:
                response = "Invalid command"
            else:
                command = request[0].upper()
                
                if command == "SET" and len(request) == 3:
                    key, value = request[1], request[2]
                    store[key] = value
                    response = f"Key {key} set to {value}"
                elif command == "GET" and len(request) == 2:
                    key = request[1]
                    value = store.get(key, "Key not found")
                    response = f"Value for {key}: {value}"
                elif command == "DELETE" and len(request) == 2:
                    key = request[1]
                    if key in store:
                        del store[key]
                        response = f"Key {key} deleted"
                    else:
                        response = "Key not found"
                else:
                    response = "Invalid command"
            
            # Step 3: Sending Responses
            conn.sendall(response.encode())

def start_server(host='127.0.0.1', port=65432):
    # Step 1: Socket Creation
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to address and port
    server_socket.bind((host, port))
    
    # Enable the server to accept connections
    server_socket.listen()

    print(f"Server started and listening on {host}:{port}")
    
    while True:
        # Accept a connection (Blocking call, waits until a client connects)
        conn, addr = server_socket.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    start_server()
