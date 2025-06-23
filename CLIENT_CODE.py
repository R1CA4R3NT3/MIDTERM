import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print(f"Server listening on host{HOST}:port{PORT}...")
    message = "Hello, Server!"
    client_socket.sendall(message.encode())
    data = client_socket.recv(1024)
    print(f"Received from server: {data.decode()}")
    