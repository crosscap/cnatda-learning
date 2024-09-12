#! /usr/bin/env python3
from socket import *
import base64


msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
fromMail = 'xxx@163.com'
toMail = 'xxx'

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.163.com'
stmpPort = 25

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
account = base64.b64encode(fromMail.encode()).decode() + "\r\n"
secretCode = base64.b64encode('secret!'.encode()).decode() + "\r\n"
authCommand = 'AUTH LOGIN\r\n'
clientSocket.send(authCommand.encode())
recv2_1 = clientSocket.recv(1024).decode()
if recv2_1[:3] != '334':
    print('334 reply not received from server.')
print(recv2_1)
clientSocket.send(account.encode())
recv2_2 = clientSocket.recv(1024).decode()
print(recv2_2)
if recv2_2[:3] != '334':
    print('334 reply not received from server.')
clientSocket.send(secretCode.encode())
recv2_3 = clientSocket.recv(1024).decode()
print(recv2_3)
if recv2_3[:3] != '235':
    print('235 reply not received from server.')

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
