import socket
import datetime

def daytime_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Daytime server is listening on port", port)
    
    while True:
        client_socket, client_address = server_socket.accept()
        print("Connection from:", client_address)
        
        try:
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            client_socket.sendall(current_time.encode('ascii'))
        except Exception as e:
            print("Error:", e)
        finally:
            client_socket.close()

if __name__ == "__main__":
    host = '0.0.0.0'
    port = 12345
    
    daytime_server(host, port)
# PS C:\Users\aryan> netstat -an | findstr "12345"
#   TCP    0.0.0.0:12345          0.0.0.0:0              LISTENING
# Get-NetTCPConnection -LocalPort 12345
