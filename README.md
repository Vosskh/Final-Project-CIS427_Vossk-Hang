# CIS 427: Multi-User Secure Chat Service
**Winter 2026 Final Project**

## Team Members
* **Member Name:** Vossk Hang (Solo)

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
   `python server.py`
2. **Start Multiple Clients:**
   `python client.py`

## Video Demonstration
- *Included in the submission .Zip folder and this repo.*

## Design Strategy
- **Refer to the Programming_Memo.pdf for a detailed threading model and protocol analysis.**

## Submission Checklist for Students
- [x] **GitHub Repository:** Contains source code and the 3-minute video demo.
- [x] **Canvas Upload:** A single .zip file containing the source code and the Programming_Memo.pdf.
- [x] **Ethics Section:** Ensure the Design Memo includes a discussion on data privacy and encryption.

## 1. Feature Checklist by Component

### A. Server-Side Features (`server.py`)
- [x] **Socket Initialization:** Create a TCP welcoming socket using `AF_INET` and `SOCK_STREAM`.
- [x] **Address Binding:** Bind the server to a specific port (5555) and host.
- [x] **Connection Listening:** Implement `.listen()` to queue incoming requests.
- [x] **Multi-threaded Handling:** Spawn a new `threading.Thread` for every individual client.
- [x] **Client Registry:** Maintain a data structure (e.g., a list/dict) to store active sockets.
- [x] **Broadcast Functionality:** Iterate through the list to send messages to everyone *except* the sender.
- [x] **Graceful Disconnect Logic:** Detect closed sockets, remove them from the list, and close server-side.

### B. Client-Side Features (`client.py`)
- [x] **Dual-Threaded Operation:** - **Listener Thread:** Constant `.recv()` to show messages instantly.
    - **Sender Thread:** Main loop for user `input()`.
- [x] **User Interface:** Terminal-based prompts for name and message entry.
- [x] **Privacy Disclaimer:** Print an ethical/legal disclaimer upon launch (CAC 4).

### C. Application Protocol & Reliability (IO 6)
- [x] **Message Framing:** Implement header format: `LENGTH|SENDER|MESSAGE`.
- [x] **Framing Parser:** Logic to unpack headers and display the sender and message separately.
- [x] **Heartbeat Sender (Client):** Send "HEARTBEAT" every 10 seconds.
- [x] **Heartbeat Monitor (Server):** Logic to drop clients if no activity is detected for 20 seconds.

## 2. Implementation Roadmap
 - **Phase 1: Connectivity (Completed):** Establish a 1-to-1 TCP handshake between client and server.
 - **Phase 2: Concurrency (Completed):** Enable the server to accept multiple clients using threading.
 - **Phase 3: The "Broadcast" Logic (Completed):** Update the server to relay messages to all active clients in the registry.
 - **Phase 4: Protocol & Parsing (Completed):** Implement the `LENGTH|SENDER|MESSAGE` framing.
 - **Phase 5: Reliability & Cleanup (Completed):** Code the server-side timer to drop inactive clients.
 - **Phase 6: Final Polish (Completed):** Add the CAC 4 Privacy disclaimer and finalize the Programming Memo.

## 3. Implementation Status Summary
**Fully Implemented.** All core requirements, including protocol framing, broadcast management, concurrent threading, and heartbeat timeout reliability logic, have been successfully coded and tested.
