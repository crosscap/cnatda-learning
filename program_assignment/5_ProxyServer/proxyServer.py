#! /usr/bin/env python3

from socket import *
import sys


if len(sys.argv) <= 1:
    print('Usage : "python ProxyServer.py server_ip"\n')
    print('[server_ip : It is the IP Address Of Proxy Server')
    sys.exit(2)

# Create a server socket, bind it to a port and start listening
serverPort = 80
proxyPort = 8888
# proxyAddress = sys.argv[1]
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(('', proxyPort))
tcpSerSock.listen(1)

while 1:
    # Strat receiving data from the client
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from:', addr)
    message = tcpCliSock.recv(1024).decode()
    print(message)              # first line: GET /www.google.com HTTP/1.1
    # Extract the filename from the given message
    print(message.split()[1])   # /www.google.com
    filename = message.split()[1].partition("/")[2]
    print(filename)             # www.google.com
    fileExist = "false"
    filetouse = "/" + filename  # /www.google.com
    print(filetouse)
    try:
        # Check wether the file exist in the cache
        f = open(filetouse[1:], "r")
        outputdata = f.readlines()
        fileExist = "true"
        # ProxyServer finds a cache hit and generates a response message
        tcpCliSock.send("HTTP/1.0 200 OK\r\n".encode())
        tcpCliSock.send("Content-Type:text/html\r\n".encode())
        tcpCliSock.send("\r\n".encode())
        for i in range(0, len(outputdata)):
            tcpCliSock.send(outputdata[i].encode())
        print('Read from cache')
    # Error handling for file not found in cache
    except IOError:
        if fileExist == "false":
            # Create a socket on the proxyserver
            c = socket(AF_INET, SOCK_STREAM)
            hostn = filename.replace("www.", "", 1)
            print(hostn)        # google.com
            try:
                # Connect to the socket to port 80
                serverAddress = gethostbyname(hostn)
                c.connect((serverAddress, serverPort))
                print('connect to server')
                # Create a temporary file on this socket and ask port 80 for the file requested by the client
                # fileobj = c.makefile('w', 0)
                # fileobj.write("GET "+"http://" + filename + " HTTP/1.0\n\n")
                # Read the response into buffer
                toServerData = "GET "+"http://" + filename + " HTTP/1.0\n\n"
                c.send(toServerData.encode())
                messageFromServer = c.recv(1024).decode()
                c.close()
                # Create a new file in the cache for the requested file.
                # Also send the response in the buffer to client socket and the corresponding file in the cache
                tmpFile = open("./" + filename, "wb")
                tmpFile.write(messageFromServer.encode())
                tmpFile.close()
                f = open("./" + filename, "r")
                toClientData = f.readlines()
                for i in range(0, len(toClientData)):
                    tcpCliSock.send(toClientData[i].encode())
                f.close()
                print('read from server')
            except:
                print("Illegal request")
        else:
            # HTTP response message for file not found
            status_line = "HTTP/1.1 404 Not Found\r\n\r\n"
            headers = f"Content-Type: text/html; charset=UTF-8\r\n"
            head = status_line + headers + "\r\n"
            tcpCliSock.send(head.encode())
            body = "404 Not Found\r\n"
            tcpCliSock.send(body.encode())
            print('file not found')
    # Close the client and the server sockets
    tcpCliSock.close()

print('proxy closed!')
tcpSerSock.close()
