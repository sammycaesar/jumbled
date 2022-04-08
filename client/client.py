import sys
import socket


# Initialisation
HOST = "127.0.0.1"
PORT =  3000
FORMAT = 'ASCII'
HEADER = 64
SIZE = 1024

# Connect to the client
try: 
    # 1. Create socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #2. Establish connection
    client.connect((HOST, PORT))

    #3. Send data to socket and encode
    client.send('Hello World'.encode(FORMAT))
    data = client.recv(SIZE)
    data = data.decode()

    #4. Close connection
    client.close()

    print('Data recieved: {}'.format(data))
    print('Socket is now closed')

except socket.error as err: 
   print("Could not connect to server with the error %s*" %(err))
   sys.exit();   