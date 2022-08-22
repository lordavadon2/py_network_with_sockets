# Chat Server Module
import socket


HOSTNAME = socket.gethostname()
HOST_IP = socket.gethostbyname(HOSTNAME)
HOST_PORT = 12345
ENCODER = 'utf-8'
BYTESIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

print(f'Server started on: {HOST_IP}:{HOST_PORT}')
print('=' * 30)
client_socket, client_address = server_socket.accept()
print(f'Connected to {":".join(map(str, client_address))}')
client_socket.send(f'You are connected to {HOST_IP}!'.encode(ENCODER))

while True:
    message = client_socket.recv(BYTESIZE).decode(ENCODER)

    if message == 'quit':
        client_socket.send('quit'.encode(ENCODER))
        print('Ending chat!')
        break
    else:
        print(message)
        message = input('Message: ')
        client_socket.send(message.encode(ENCODER))

client_socket.close()
