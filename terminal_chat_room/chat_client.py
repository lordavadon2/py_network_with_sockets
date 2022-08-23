# Chat Client Module
import socket, threading


SERVER_IP = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 12345
ENCODER = 'utf-8'
BYTESIZE = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))


def send_message():
    """
    Send message to the server
    """
    while True:
        message = input()
        client_socket.send(message.encode(ENCODER))


def receive_message():
    """
    Receive message from the server
    """
    while True:
        try:
            message = client_socket.recv(BYTESIZE).decode(ENCODER)

            if message == 'NAME':
                name = input('What is your name: ')
                client_socket.send(name.encode(ENCODER))
            else:
                print(message)
        except:
            print('An error occurred')
            client_socket.close()
            break


received_thread = threading.Thread(target=receive_message).start()
send_thread = threading.Thread(target=send_message).start()
