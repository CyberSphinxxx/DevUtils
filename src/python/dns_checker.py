import socket

def get_dns_records(domain):
    """
    Retrieves DNS records for a given domain.
    """
    records = {}
    try:
        records['A'] = socket.gethostbyname(domain)
    except socket.gaierror:
        records['A'] = "Not found"
    
    return records

if __name__ == "__main__":
    domain = "google.com"
    print(f"DNS records for {domain}:")
    print(get_dns_records(domain))
