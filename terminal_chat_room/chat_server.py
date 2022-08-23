# Chat Server Module
import socket, threading

# Define constants to be used
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = 'utf-8'
BYTESIZE = 1024

# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

# Create two blank lists to store connected client sockets and their names
client_socket_list = []
client_name_list = []


def broadcast_message(message):
    """
    Send message to ALL clients who connected to server
    """
    message = message.encode(ENCODER)
    for client_socket in client_socket_list:
        client_socket.send(message)


def receive_message(client_socket):
    """
    Receive incoming message from client
    """
    while True:
        try:
            index = client_socket_list.index(client_socket)
            name = client_name_list[index]

            message = client_socket.recv(BYTESIZE).decode(ENCODER)
            message = f"\033[1;92m\t{name}: {message}\033[0m"
            broadcast_message(message)
        except:
            index = client_socket_list.index(client_socket)
            name = client_name_list[index]

            client_socket_list.remove(client_socket)
            client_name_list.remove(name)

            client_socket.close()

            broadcast_message(f"\033[5;91m\t{name} has left the chat!\033[0m")
            break


def connect_client():
    """
    Connect an incoming client to the server
    """
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connected with {':'.join(map(str, client_address))}...")

        client_socket.send("NAME".encode(ENCODER))
        client_name = client_socket.recv(BYTESIZE).decode(ENCODER)

        client_socket_list.append(client_socket)
        client_name_list.append(client_name)

        print(f"Name of new client is {client_name}\n")
        client_socket.send(f"{client_name}, you have connected to the server!".encode(ENCODER))
        broadcast_message(f"{client_name} has joined the chat!")

        receive_thread = threading.Thread(target=receive_message, args=(client_socket,))
        receive_thread.start()


# Start the server
print(f'Server started on: {HOST_IP}:{HOST_PORT}')
print('=' * 30)
connect_client()
