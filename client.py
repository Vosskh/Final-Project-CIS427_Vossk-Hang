import socket
import threading
import time
import sys

is_quitting = False 

def print_ethics_disclaimer():
    """Prints a privacy and ethics disclaimer on launch (CAC 4)."""
    print("="*60)
    print(" ETHICS & PRIVACY DISCLAIMER [CAC 4]")
    print("="*60)
    print("Notice: This is a peer-to-peer style broadcast chat service.")
    print("Data transmitted over this network is NOT end-to-end encrypted.")
    print("Please do not share sensitive personal information, passwords,")
    print("or financial data. By continuing, you acknowledge these terms.")
    print("="*60 + "\n")

def receive_messages(client_socket):
    """Continuously listens for messages from the server and parses the framing."""
    global is_quitting
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
                
            parts = data.split('|', 2)
            if len(parts) == 3:
                msg_length, sender, message = parts
                print(f"\r[{sender}]: {message}".ljust(50))
                print("Enter message: ", end="", flush=True) 
        except Exception:
            if not is_quitting:
                print("\n[ERROR] Connection to server lost.")
            client_socket.close()
            break # Changed from sys.exit(0) to just break the loop cleanly

def send_heartbeat(client_socket):
    """Sends a keep-alive signal every 10 seconds."""
    while True:
        time.sleep(10)
        try:
            client_socket.send("HEARTBEAT".encode('utf-8'))
        except:
            break 

def start_client():
    global is_quitting
    
    print_ethics_disclaimer()
    
    username = input("Enter your chat username: ").strip()
    if not username:
        username = "Anonymous"

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(('localhost', 5555))
    except ConnectionRefusedError:
        print("[ERROR] Could not connect to the server. Is server.py running?")
        return

    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()
    threading.Thread(target=send_heartbeat, args=(client,), daemon=True).start()

    print("\n[SUCCESS] Connected to chat! You can start typing messages.\n")
    
    while True:
        try:
            msg = input("Enter message: ")
            if msg.lower() == '/quit':
                is_quitting = True
                client.close()
                sys.exit(0)
                
            if msg:
                formatted_msg = f"{len(msg)}|{username}|{msg}"
                client.send(formatted_msg.encode('utf-8'))
        except KeyboardInterrupt:
            is_quitting = True
            client.close()
            sys.exit(0)
        except Exception as e:
            print(f"Failed to send message: {e}")
            break

if __name__ == "__main__":
    start_client()