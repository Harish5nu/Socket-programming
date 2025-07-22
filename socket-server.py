import socket
import threading

# Function to receive messages from the client
def receive_messages(conn):
    while True:
        try:
            # Receive message from client
            message = conn.recv(1024).decode()
            if message:
                print("Client:", message)
        except:
            print("Client disconnected.")
            break

# Create a server socket
server_socket = socket.socket()  # Default: AF_INET, SOCK_STREAM
host = 'localhost'
port = 12345

# Bind the socket to address and port
server_socket.bind((host, port))
server_socket.listen(1)  # Accept 1 connection at a time
print("Server is waiting for a client to connect...")

# Accept connection from client
conn, addr = server_socket.accept()
print("Connected to client at:", addr)

# Start a thread to receive messages from client
threading.Thread(target=receive_messages, args=(conn,)).start()

# Main loop to send messages to client
while True:
    msg = input("You: ")
    conn.send(msg.encode())  # Send encoded message to client
