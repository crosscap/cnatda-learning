from socket import *

serverName = '192.168.31.156'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modefiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modefiedMessage.decode())
clientSocket.close()
