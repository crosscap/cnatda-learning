#! /usr/bin/env python3

import time
from socket import *


# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.bind(('', 23711))
clientSocket.settimeout(1)

serverName = 'localhost'
serverPort = 12000

for i in range(0, 10):
    start_time = time.time()
    send_message = "Ping " + f"{i} " + f"{start_time}"
    clientSocket.sendto(send_message.encode(), (serverName, serverPort))
    try:
        message, address = clientSocket.recvfrom(1024)
    except TimeoutError:
        print("Request timed out")
        continue
    end_time = time.time()
    print(message.decode())
    print(f"spent {end_time - start_time} seconds")
