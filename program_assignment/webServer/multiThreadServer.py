#! /usr/bin/env python3

# import socket module
from socket import *
import threading
import time
import sys  # In order to terminate the program


class send_message(threading.Thread):
    """ The class that help main thread to creat child thread.
    """

    def __init__(self, connectionSocket) -> None:
        super().__init__()
        self.connectionSocket = connectionSocket

    def run(self) -> None:
        try:
            message = self.connectionSocket.recv(1024).decode()
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()

            # Send one HTTP header line into socket
            status_line = "HTTP/1.1 200 OK\r\n"
            date = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())
            headers = f"Date: {date}\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n"
            head = status_line + headers
            self.connectionSocket.send(head.encode())

            # Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                self.connectionSocket.send(outputdata[i].encode())
            self.connectionSocket.send("\r\n".encode())

            self.connectionSocket.close()
        except IOError:
            # Send response message for file not found
            status_line = "HTTP/1.1 404 Not Found\r\n\r\n"
            date = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())
            headers = f"Date: {date}\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n"
            head = status_line + headers
            self.connectionSocket.send(head.encode())
            body = "404 Not Found\r\n"
            self.connectionSocket.send(body.encode())

            # Close client socket
            self.connectionSocket.close()
        except KeyboardInterrupt:
            self.connectionSocket.close()
            raise KeyboardInterrupt


def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a sever socket
    serverPort = 23711
    serverSocket.bind(('', serverPort))
    serverSocket.listen(3)

    try:
        while True:
            # Establish the connection
            print('Ready to serve...')
            connectionSocket, addr = serverSocket.accept()
            childThread = send_message(connectionSocket)

            childThread.start()
    except KeyboardInterrupt:
        serverSocket.close()
        sys.exit()  # Terminate the program after sending the corresponding data

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == '__main__':
    main()
