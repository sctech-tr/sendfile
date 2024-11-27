import socket

def get_local_ip():
    """Get the local IP address of the machine."""
    try:
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    except Exception as e:
        return f"Error retrieving IP: {e}"
