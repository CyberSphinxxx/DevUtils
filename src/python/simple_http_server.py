import http.server
import socketserver
import sys

def start_server(port=8000):
    """Starts a simple HTTP server."""
    Handler = http.server.SimpleHTTPRequestHandler
    try:
        with socketserver.TCPServer(("", port), Handler) as httpd:
            print(f"Serving at port {port}")
            httpd.serve_forever()
    except OSError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    port = 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Invalid port number.")
    
    start_server(port)
