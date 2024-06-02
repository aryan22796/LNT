import socket

def start_client(host='127.0.0.1', port=65432):
    # Step 1: Socket Creation
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Step 2: Connection Establishment
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")

    try:
        # Step 3: Sending Requests
        message = "Hello, Server!"
        client_socket.sendall(message.encode())
        print(f"Sent request: {message}")
        
        # Step 4: Receiving Responses
        data = client_socket.recv(1024)
        print(f"Received response: {data.decode()}")
        
        # Step 5: Processing Responses (In this case, just printing the response)
    finally:
        # Step 6: Closing the Connection
        client_socket.close()
        print("Client connection closed.")

if __name__ == "__main__":
    start_client()
