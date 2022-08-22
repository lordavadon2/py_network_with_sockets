# TCP Client Module
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f'Hostname: {socket.gethostname()}')
print(f'IP address: {socket.gethostbyname(socket.gethostname())}')

client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345))

message = client_socket.recv(1024)
print(message.decode('utf-8'))

client_socket.close()
