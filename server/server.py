import socket
import threading


# Initialisation
HOST = "127.0.0.1"
PORT =  3000
FORMAT = 'ASCII'
HEADER = 64
SIZE = 1024

# Connect to the server
# 1. Create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#2. Establish connection
client.bind((HOST, PORT))
client.listen(1)

print('Listening on {}:{}'.format(HOST, PORT))


def manage_client(client_socket):
    request = client_socket.recv(SIZE)
    print('Received {}'.format(request))
    client_socket.send('Woo Success')
    client_socket.close()




 