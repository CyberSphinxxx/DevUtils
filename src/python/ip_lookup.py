import socket
import requests

def get_ip_info(ip_address):
    """
    Retrieves information about an IP address using a public API.
    """
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def get_local_ip():
    """
    Gets the local IP address of the machine.
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return "127.0.0.1"

if __name__ == "__main__":
    local_ip = get_local_ip()
    print(f"Local IP: {local_ip}")
    print("Info for 8.8.8.8:")
    print(get_ip_info("8.8.8.8"))
