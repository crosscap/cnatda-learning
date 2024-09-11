#! /usr/bin/env python3

import time
from socket import *
import sys


# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
# Set the time that wait for client's heart beat
serverSocket.settimeout(10)

last_seq = None
last_time = None
while True:
    try:
        message, address = serverSocket.recvfrom(1024)
    except TimeoutError:
        print("clinet have been closed!")
        serverSocket.close()
        sys.exit()
    sequence_number = int(message.decode().split()[1])
    send_time = float(message.decode().split()[2])
    if last_seq is not None:
        for i in range(last_seq + 1, sequence_number):
            print(f"package {i} missed!")
        print(f"{send_time - last_time} seconds passed to get {sequence_number}!")
    else:
        for i in range(0, sequence_number):
            print(f"package {i} missed!")
        print(f"{sequence_number} is the first seceived package!")

    last_seq = sequence_number
    last_time = send_time
