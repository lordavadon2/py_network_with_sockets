# UDP Client Module
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f'Hostname: {socket.gethostname()}')
print(f'IP address: {socket.gethostbyname(socket.gethostname())}')

client_socket.sendto('Hello UDP server!'.encode('utf-8'), (socket.gethostbyname(socket.gethostname()), 54321))

client_socket.close()
