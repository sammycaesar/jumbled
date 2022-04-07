import socket, ssl, threading, random

host, port = sys.argv[1], int(sys.argv[2])

HEADER = 64
format = 'ascii'