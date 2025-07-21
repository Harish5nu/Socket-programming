import socket

# Create socket
client_socket = socket.socket()
host = 'localhost'
port = 12345

# Connect to the server
client_socket.connect((host, port))

# Send message to server
client_socket.send("Hello from client!".encode())

# Receive reply
data = client_socket.recv(1024).decode()
print("Server says:", data)

# Close connection
client_socket.close()
