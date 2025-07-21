import socket

# Create socket
server_socket = socket.socket()
host = 'localhost'
port = 12345

# Bind the socket to a port
server_socket.bind((host, port))
server_socket.listen(1)

print("Server is waiting for a connection...")

# Accept a client connection
conn, addr = server_socket.accept()
print("Connected with:", addr)

# Receive message from client
data = conn.recv(1024).decode()
print("Client says:", data)

# Send a reply
conn.send("Hello from server!".encode())

# Close connection
conn.close()
