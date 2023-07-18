import socket

# get ipv4 for VMware
# HOST = socket.gethostbyname(socket.gethostname())
HOST = '192.168.8.124'  # always server ip
PORT = 9090

# SOCK_STREAM -> tcp
# AF_INET -> IPv4

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.send("Hello".encode('utf-8'))
print(client.recv(1024).decode('utf-8'))