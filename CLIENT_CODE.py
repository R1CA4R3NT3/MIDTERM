import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

# Connect to a local server, send a message, and receive a response.
# Handle exceptions for connection errors and unexpected issues.
# Perform graceful shutdown handling

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print(f"Connected to server at host {HOST}:port {PORT}...")

        message = "Hello, Server!"
        client_socket.sendall(message.encode())

        data = client_socket.recv(1024)
        print(f"Received from server: {data.decode()}")

except ConnectionRefusedError:
    print("Connection failed: Server is not available.")
except socket.error as e:
    print(f"Socket error occurred: {e}")
except Exception as ex:
    print(f"Unexpected error: {ex}")
finally:
    print("Client shutdown complete.")