#! /usr/bin/env python3

import random
import time
from socket import *


# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.bind(('', 23711))
clientSocket.settimeout(1)

serverName = 'localhost'
serverPort = 12000

for i in range(0, 10):
    if random.randint(0, 10) < 4:
        continue
    send_time = time.time()
    send_message = "Ping " + f"{i} " + f"{send_time}"
    clientSocket.sendto(send_message.encode(), (serverName, serverPort))

clientSocket.close()
