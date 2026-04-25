import socket
import threading
import time

# List to keep track of active client connections
clients = [] 

def broadcast(message, sender_socket):
    """Broadcasts message to all clients except the sender [cite: 404]"""
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

def handle_client(client_socket):
    """Handles continuous message receiving from a specific client [cite: 403]"""
    while True:
        try:
            # Implement Message Framing: LENGTH|SENDER|MESSAGE [cite: 405]
            data = client_socket.recv(1024)
            if data:
                broadcast(data, client_socket)
        except:
            break

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5555))
    server.listen()
    print("Server is listening on port 5555...")

    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        # Start a new thread for each client [cite: 403, 418]
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    start_server()
