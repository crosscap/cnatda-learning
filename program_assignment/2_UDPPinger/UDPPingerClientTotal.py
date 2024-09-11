#! /usr/bin/env python3

import time
from socket import *


# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.bind(('', 23711))
clientSocket.settimeout(1)

serverName = 'localhost'
serverPort = 12000

RTT_max = 0
RTT_min = 100
RTT_sum = 0
success_cnt = 0

for i in range(0, 10):
    start_time = time.time()
    send_message = "Ping " + f"{i} " + f"{start_time}"
    clientSocket.sendto(send_message.encode(), (serverName, serverPort))
    try:
        message, address = clientSocket.recvfrom(1024)
    except TimeoutError:
        continue
    end_time = time.time()
    RTT_recent = end_time - start_time
    RTT_max = max(RTT_max, RTT_recent)
    RTT_min = min(RTT_min, RTT_recent)
    RTT_sum += RTT_recent
    success_cnt += 1

print(f"max RTT: {RTT_max} seconds")
print(f"min RTT: {RTT_min} seconds")
print(f"average RTT: {RTT_sum / success_cnt} seconds")
print(f"success rate: {success_cnt * 10}%")

clientSocket.close()
