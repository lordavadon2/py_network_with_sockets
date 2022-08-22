# TCP Server Module
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f'Hostname: {socket.gethostname()}')
print(f'IP address: {socket.gethostbyname(socket.gethostname())}')

server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

server_socket.listen()

while True:
    client_socket, client_address = server_socket.accept()

    print(f'Connected to {":".join(map(str, client_address))}')

    client_socket.send('You are connected!'.encode('utf-8'))

    server_socket.close()
    break
