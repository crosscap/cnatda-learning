#! /usr/bin/env python3

from socket import *
import time
import sys


def main():
    if len(sys.argv) != 4:
        print("you should type in right num of args!")
        sys.exit()
    print("getting message...")
    serverAddress = sys.argv[1]
    serverPort = int(sys.argv[2])
    requiredFile = sys.argv[3]

    clinetSocket = socket(AF_INET, SOCK_STREAM)
    clinetSocket.connect((serverAddress, serverPort))

    date = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())
    request_line = f"GET {requiredFile} HTTP/1.1\r\n"
    headers = f"Host: {serverAddress}:{serverPort}\r\n"
    headers += f"Date: {date}\r\n\r\n"
    head = request_line + headers

    clinetSocket.send(head.encode())

    receivedFile = clinetSocket.recv(2048)
    while receivedFile:
        print(receivedFile.decode())
        receivedFile = clinetSocket.recv(2048)

    clinetSocket.close()
    sys.exit()


if __name__ == '__main__':
    main()
