import socket

# get ipv4 for VMware
# HOST = socket.gethostbyname(socket.gethostname())
HOST = '192.168.8.124'
PORT = 9090

# SOCK_STREAM -> tcp
# AF_INET -> IPv4

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)  # limit number of connections

while True:
    communication_socket, address = server.accept()
    print(f"Connected to {address}")
    incom_message = communication_socket.recv(1024).decode('utf-8')
    print(f"Message from client is: {incom_message}")
    out_message = 'Got your message!, Thank you'
    communication_socket.send(out_message.encode('utf-8'))
    communication_socket.close()
    print(f"Connection with {address} ended!")
