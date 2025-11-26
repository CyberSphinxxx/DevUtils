import socket
import sys

def scan_ports(target, ports):
    """
    Scans specified ports on a target IP.
    """
    print(f"Scanning {target}...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: Open")
        else:
            print(f"Port {port}: Closed")
        sock.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python port_scanner.py <target_ip> [ports...]")
    else:
        target = sys.argv[1]
        ports = [int(p) for p in sys.argv[2:]] if len(sys.argv) > 2 else [80, 443, 22, 21, 8080]
        scan_ports(target, ports)
