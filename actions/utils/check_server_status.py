import socket

def check_server_status(url, port):
    try:
        
        socket.create_connection((url, port), timeout=5)
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False
    
