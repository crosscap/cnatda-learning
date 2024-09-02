from socket import *

serverName = '192.168.31.156'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message = input('Input lowercase sentence:')
clientSocket.send(message.encode())
modefiedMessage = clientSocket.recv(2048)
print('From Server: ', modefiedMessage.decode())
clientSocket.close()
