[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/AHyt8oRg)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=23527036&assignment_repo_type=AssignmentRepo)
# CIS 427: Multi-User Secure Chat Service
**Winter 2026 Final Project**

## Team Members
* **Member 1 Name:** [Student Name]
* **Member 2 Name:** [Student Name]

## Project Overview
This project implements a multi-threaded client-server chat application using Python's `socket` and `threading` modules. The server acts as a central hub, broadcasting messages to all connected clients while maintaining connection reliability through a heartbeat mechanism.

## Features
- **TCP Socket Implementation:** Reliable byte-stream communication.
- **Multi-threading:** Concurrent handling of multiple client connections.
- **Message Framing:** Custom header format (`LENGTH|SENDER|MESSAGE`).
- **Heartbeat Mechanism:** Automatic cleanup of dead client sockets every 10 seconds.
- **Privacy & Ethics:** Implementation of a basic logging disclaimer regarding data privacy.

## How to Run
1. **Start the Server:**
   python server.py
2. **Start Multple Clients:**
   python client.py
## Video Demonstration
- **Link to YouTube/GitHub video showing 3 clients chatting at once**
## Design Strategy
- **Refer to the Design_Memo.pdf for a detailed threading model and protocol analysis.**

## Submission Checklist for Students
- **Ensure the following are completed before April 23, 2026:**
- **GitHub Repository: Contains source code and the 3-minute video demo.**
- **Canvas Upload: A single .zip file containing the source code and the Design_Memo.pdf.**
- **Ethics Section: Ensure the Design Memo includes a discussion on data privacy and encryption.**

## 1. Feature Checklist by Component

### A. Server-Side Features (`server.py`)
- [x] **Socket Initialization:** Create a TCP welcoming socket using `AF_INET` and `SOCK_STREAM`.
- [x] **Address Binding:** Bind the server to a specific port (5555) and host.
- [x] **Connection Listening:** Implement `.listen()` to queue incoming requests.
- [x] **Multi-threaded Handling:** Spawn a new `threading.Thread` for every individual client.
- [ ] **Client Registry:** Maintain a data structure (e.g., a list) to store active sockets.
- [ ] **Broadcast Functionality:** Iterate through the list to send messages to everyone *except* the sender.
- [ ] **Graceful Disconnect Logic:** Detect closed sockets, remove them from the list, and close server-side.

### B. Client-Side Features (`client.py`)
- [x] **Dual-Threaded Operation:** - **Listener Thread:** Constant `.recv()` to show messages instantly.
    - **Sender Thread:** Main loop for user `input()`.
- [ ] **User Interface:** Terminal-based prompts for name and message entry.
- [ ] **Privacy Disclaimer:** Print an ethical/legal disclaimer upon launch (CAC 4).

### C. Application Protocol & Reliability (IO 6)
- [ ] **Message Framing:** Implement header format: `LENGTH|SENDER|MESSAGE`.
- [ ] **Framing Parser:** Logic to unpack headers and display the sender and message separately.
- [x] **Heartbeat Sender (Client):** Send "HEARTBEAT" every 10 seconds.
- [ ] **Heartbeat Monitor (Server):** Logic to drop clients if no activity is detected for 20 seconds.

## 2. Implementation Roadmap
 - **Phase 1: Connectivity (Completed in Template):**
   * Establish a 1-to-1 TCP handshake between client and server.
 - **Phase 2: Concurrency (Completed in Template):**
   * Enable the server to accept multiple clients using threading.
 - **Phase 3: The "Broadcast" Logic (Student Task):**
   * Update the server to relay messages to all active clients in the registry.
 - **Phase 4: Protocol & Parsing (Student Task):**
   * Implement the `LENGTH|SENDER|MESSAGE`framing on the sender side and the parser on the receiver side.
 - **Phase 5: Reliability & Cleanup (Student Task):**
   * Code the server-side timer to drop inactive clients (2 missed heartbeats).
 - **Phase 6: Final Polish (Student Task):**
   * Add the CAC 4 Privacy disclaimer and finalize the Design Memo.

## 3. Implementation Status Summary

### **What is ALREADY implemented (The Skeleton):**
- **The Plumbing:** Core TCP socket setup (`bind`, `listen`, `accept`, `connect`).
- **Threading Infrastructure:** The logic to spawn threads so the server doesn't block and the client can send/receive at the same time.
- **Heartbeat Interval:** The basic timing loop for the client to send signals.

### **What YOU must implement (The Core Project):**
- **The Application Protocol:** You must change raw strings into the `LENGTH|SENDER|MESSAGE` format and write the logic to decode it.
- **Broadcast Management:** You must manage the `clients` list to ensure everyone sees the chat.
- **Reliability Logic:** You must write the server-side code that tracks the 20-second timeout for each client.
- **Error Handling:** Ensure the server doesn't crash when a client unexpectedly disconnects.
- **Ethical Compliance:** Print the required privacy warnings to the terminal.
