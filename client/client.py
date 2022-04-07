import sys
from socket import *

# Initialisation
HOST = sys.argv[1]
PORT =  int(sys.argv[2])
FORMAT = 'utf-8'

# Connect to the server
try: 
    # 1. Create socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #2. Establish connection
    client.connect((HOST, PORT))

    #3. Send data to socket
    client.send(data.encode(FORMAT))

    #4. Close connection
    client.close()

    print('Data recieved: {}'.format(data))
    print('Socket is now closed')

except: 
   print("Could not connect to server")
   sys.exit();   