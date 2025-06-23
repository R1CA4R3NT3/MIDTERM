import socket
import time
import sys

def scan_ports(host, start_port, end_port):
    """
    Scans ports in a given range on the local host.

    Arguments:
        host (str): The IP address or hostname to scan.
        start_port (int): Starting port number.
        end_port (int): Ending port number.

    Returns:
        list: Open ports found during the scan.
    """
    print(f"\n Scanning {host} from port {start_port} to {end_port}...")
    open_ports = []

# Check the target host's domain name or IP address can be properly resolved 
# to a network address before attempting to connect to connect to any ports.

    try:
        socket.gethostbyname(host)
    except socket.gaierror:
        print(f"[ERROR] Could not resolve hostname: {host}")
        return open_ports

    start_time = time.time()

# Error handling for unreachable hosts.
# Error handling for invalid port numbers.

    try:
        for port in range(start_port, end_port + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)
                try:
                    result = sock.connect_ex((host, port))
                    if result == 0:
                        print(f"[OPEN] Port {port}")
                        open_ports.append(port)
                    else:
                        print(f"[CLOSED/UNREACHABLE/NO ONE HOME] Port {port}")
                except socket.timeout:
                    print(f"[TIMEOUT] Port {port} took too long to respond or is asleep.")
                except Exception as e:
                    print(f"[EXCEPTION] Port {port}: {e}")
    except KeyboardInterrupt:
        print("\n[INTERRUPTED] Scan stopped by user.")
    except Exception as e:
        print(f"[FATAL ERROR] {e}")
    finally:
        elapsed_time = time.time() - start_time
        print(f"\n Scan completed in {elapsed_time:.2f} seconds.")
        print(f"Total open ports found: {len(open_ports)}")

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