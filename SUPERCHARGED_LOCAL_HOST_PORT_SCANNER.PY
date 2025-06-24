import socket
import time
import threading
import logging

# Configure logging
logging.basicConfig(
    filename='closed_ports.log',
    filemode='w',
    level=logging.INFO,
    format='[%(asctime)s] %(message)s',
)
    
def scan_port(host, port, open_ports):
"""
    Scans ports in a given range on the local host.

    Arguments:
        host (str): The IP address or hostname to scan.
        start_port (int): Starting port number.
        end_port (int): Ending port number.

    Returns:
        list: Open ports found during the scan.
"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.2)
        try:
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"[OPEN] Port {port}")
                open_ports.append(port)
            else:
                logging.info(f"Port {port} is closed or unreachable.")
        except socket.timeout:
            logging.info(f"Port {port} timed out.")
        except Exception as e:
            logging.info(f"Port {port} exception: {e}")

def scan_ports(host, start_port, end_port):
    print(f"\nScanning {host} from port {start_port} to {end_port}...")
    open_ports = []
    threads = []

# Validate port range
    if not (0 <= start_port <= 65535 and 0 <= end_port <= 65535):
        print(f"[ERROR] Invalid port numbers. Must be in range 0-65535.")
        return open_ports
    if start_port > end_port:
        print(f"[ERROR] Start port must not be greater than end port.")
        return open_ports

# Error handling for unreachable hosts.
# Error handling for invalid port numbers.

    try:
        socket.gethostbyname(host)
    except socket.gaierror:
        print(f"[ERROR] Could not resolve hostname: {host}")
        return open_ports

    start_time = time.time()

    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(host, port, open_ports))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    elapsed_time = time.time() - start_time
    print(f"\nScan completed in {elapsed_time:.2f} seconds.")
    print(f"Total open ports found: {len(open_ports)}")

# Ask the user if they want to view the log of closed ports

    view_logs = input("Would you like to view the log of closed ports? (y/n): ").strip().lower()
    if view_logs == 'y':
        try:
            with open('closed_ports.log', 'r') as log_file:
                print("\n--- Closed Ports Log ---")
                print(log_file.read())
        except FileNotFoundError:
            print("Log file not found.")

    return open_ports

# Ensure code inside runs when the file is run directly, 
# not when it’s imported somewhere else.
# Define small, medium and larger ranges to test and measure elapsed time

if __name__ == "__main__":
    target_host = "127.0.0.1"
    ranges = [
        (20, 25),     # Small range
        (1, 100),     # Medium range
        (1, 1024),    # Larger range
    ]

    for start, end in ranges:
        scan_ports(target_host, start, end)
