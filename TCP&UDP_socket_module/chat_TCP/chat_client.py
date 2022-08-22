# Chat Client Module
import socket


SERVER_HOSTNAME = socket.gethostname()
SERVER_IP = socket.gethostbyname(SERVER_HOSTNAME)
SERVER_PORT = 12345
ENCODER = 'utf-8'
BYTESIZE = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))

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
