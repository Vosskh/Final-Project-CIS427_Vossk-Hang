import socket
import threading
import time

# Dictionary to keep track of active client connections and their last heartbeat timestamp
clients = {}
# Lock for thread-safe operations on the clients dictionary
clients_lock = threading.Lock()

def broadcast(message, sender_socket):
    """Broadcasts message to all clients except the sender."""
    with clients_lock:
        # Iterate over a list of keys to avoid runtime dictionary size change errors
        for client in list(clients.keys()):
            if client != sender_socket:
                try:
                    client.send(message)
                except:
                    disconnect_client(client)

def disconnect_client(client_socket):
    """Safely removes a client from the registry and closes their socket."""
    if client_socket in clients:
        try:
            client_socket.close()
        except:
            pass
        del clients[client_socket]
        print("[DISCONNECTED] A client socket has been cleaned up.")

def handle_client(client_socket, addr):
    """Handles continuous message receiving from a specific client."""
    print(f"[NEW CONNECTION] {addr} connected.")
    
    # Initialize the heartbeat timer for the new client
    with clients_lock:
        clients[client_socket] = time.time()
        
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break # Client disconnected normally
                
            decoded_data = data.decode('utf-8')
            
            # Check if the incoming message is just a heartbeat
            if decoded_data == "HEARTBEAT":
                with clients_lock:
                    if client_socket in clients:
                        clients[client_socket] = time.time()
            else:
                # If it's a standard chat message, broadcast it
                broadcast(data, client_socket)
        except Exception as e:
            # Socket error (e.g., forced disconnect)
            break
            
    with clients_lock:
        disconnect_client(client_socket)

def monitor_heartbeats():
    """Background thread that drops clients if they miss heartbeats (>20 seconds)."""
    while True:
        time.sleep(5) # Check every 5 seconds
        current_time = time.time()
        with clients_lock:
            for client, last_active in list(clients.items()):
                if current_time - last_active > 20:
                    print(f"[TIMEOUT] Client disconnected due to heartbeat timeout.")
                    disconnect_client(client)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Prevent address binding errors
    server.bind(('localhost', 5555))
    server.listen()
    print("[STARTING] Server is listening on port 5555...")

    # Start the background heartbeat monitor
    threading.Thread(target=monitor_heartbeats, daemon=True).start()

    while True:
        client_socket, addr = server.accept()
        # Start a new thread for each client
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()

if __name__ == "__main__":
    start_server()