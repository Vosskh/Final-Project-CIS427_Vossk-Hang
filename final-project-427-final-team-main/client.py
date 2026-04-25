import socket
import threading
import time

def receive_messages(client_socket):
    """Continuously listens for messages from the server """
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(f"\n{message}")
        except:
            print("Connection closed.")
            client_socket.close()
            break

def send_heartbeat(client_socket):
    """Sends a keep-alive signal every 10 seconds [cite: 407]"""
    while True:
        time.sleep(10)
        try:
            client_socket.send("HEARTBEAT".encode('utf-8'))
        except:
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5555))

    # Thread to receive messages without blocking input 
    threading.Thread(target=receive_messages, args=(client,)).start()
    
    # Thread for heartbeat [cite: 407]
    threading.Thread(target=send_heartbeat, args=(client,), daemon=True).start()

    while True:
        msg = input("Enter message: ")
        # Follow the header format: LENGTH|SENDER|MESSAGE [cite: 405]
        formatted_msg = f"{len(msg)}|User|{msg}"
        client.send(formatted_msg.encode('utf-8'))

if __name__ == "__main__":
    start_client()
