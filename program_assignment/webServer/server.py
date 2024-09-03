#! /usr/bin/env python3
# import socket module
from socket import *
import sys  # In order to terminate the program


serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
serverPort = 23711
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()

        # Send one HTTP header line into socket
        head = "HTTP/1.1 200 OK\r\n\r\n"
        connectionSocket.send(head.encode())

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
        print("file sended")
        break
    except IOError:
        # Send response message for file not found
        head = "HTTP/1.1 404 Not Found\r\n\r\n"
        connectionSocket.send(head.encode())
        body = "404 Not Found\r\n"
        connectionSocket.send(body.encode())

        # Close client socket
        connectionSocket.close()
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
