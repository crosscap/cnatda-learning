#! /usr/bin/env python3
from socket import *
import base64


msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
fromMail = 'xxx@gmail.com'
toMail = 'xxx'

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.gmail.com'
stmpPort = 587

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, stmpPort))

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# authority account and print server response.
startTLSCommand = 'STARTTLS\r\n'
clientSocket.send(startTLSCommand.encode())
recv2 = clientSocket.recv(1024).decode()
if recv2[:3] != '220':
    print('220 reply not received from server.')
print(recv2)

# Send MAIL FROM command and print server response.
fromCommand = f'MAIL FROM: <{fromMail}>\r\n'
clientSocket.send(fromCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
toCommand = f'RCPT TO: <{toMail}>\r\n'
clientSocket.send(toCommand.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '354':
    print('354 reply not received from server.')

# Send message data.
head = f"From: {fromMail}\r\n"
head += f"To: {toMail}\r\n"
head += "Subject: A simple test\r\n"
clientSocket.send(head.encode())
clientSocket.send(msg.encode())

# Message ends with a single period.
clientSocket.send(endmsg.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)

# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv7 = clientSocket.recv(1024).decode()
print(recv7)
if recv7[:3] != '221':
    print('221 reply not received from server.')

print("Sent finished!")
clientSocket.close()
