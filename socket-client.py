import socket
import threading

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            # Receive message from server
            message = client_socket.recv(1024).decode()
            if message:
                print("Server:", message)
        except:
            print("Disconnected from server.")
            break

# Create a client socket
client_socket = socket.socket()  # Default: AF_INET, SOCK_STREAM
host = 'localhost'
port = 12345

# Connect to server
client_socket.connect((host, port))
print("Connected to the server.")

# Start a thread to receive messages from server
threading.Thread(target=receive_messages, args=(client_socket,)).start()

# Main loop to send messages to server
while True:
    msg = input("You: ")
    client_socket.send(msg.encode())  # Send encoded message to server
