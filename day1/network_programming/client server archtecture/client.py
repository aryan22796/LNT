import socket

def start_server(host='127.0.0.1', port=65432):
    # Step 1: Socket Creation
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to address and port
    server_socket.bind((host, port))
    
    # Enable the server to accept connections (listen for incoming connections)
    server_socket.listen()

    print(f"Server started and listening on {host}:{port}")

    # Accept a connection (Blocking call, waits until a client connects)
    conn, addr = server_socket.accept()
    with conn:
        print(f"Connected by {addr}")
        
        while True:
            # Step 4: Receiving Requests
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received request: {data.decode()}")
            
            # Step 5: Processing Requests (For example, simply echoing back the received data)
            response = f"Server received: {data.decode()}"
            
            # Step 3: Sending Responses
            conn.sendall(response.encode())
    
    # Step 6: Closing the Connection
    server_socket.close()
    print("Server connection closed.")

if __name__ == "__main__":
    start_server()
