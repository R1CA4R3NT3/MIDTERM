import socket

HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

# Properly create socket object (IPv4, TCP),bind to host and port, listen for incoming connections, and accept a connection
# from a client. Once connected, receive data from the client and echo it back.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server listening on host{HOST}:port{PORT}...")
    
    conn, addr = server_socket.accept()
    with conn:
        print(f"Connected by address{addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received from client: {data.decode()}")
            conn.sendall(data)  # Echo back to client