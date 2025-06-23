import socket

HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

# Create socket object (IPv4, TCP),bind to host and port, and listen for incoming connections
# Accept a connection from a client, receive data from the client and echo it back. 
# Handle exceptions for connection errors and unexpected issues.
# Perform graceful shutdown handling

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server listening on host {HOST}:port {PORT}...")

    conn, addr = server_socket.accept()
    with conn:
        print(f"Connected by address {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                print("Client disconnected.")
                break
            print(f"Received from client: {data.decode()}")
            conn.sendall(data) # Echo back to client 

except KeyboardInterrupt:
    print("\nServer manually interrupted. Shutting down...")
except socket.error as e:
    print(f"Socket error occurred: {e}")
except Exception as ex:
    print(f"Unexpected error: {ex}")
finally:
    server_socket.close()
    print("Server socket closed.")
