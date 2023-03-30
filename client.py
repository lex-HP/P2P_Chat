from socket import *


IP_addr = "10.239.229.103"
serverSocket =  socket(AF_INET, SOCK_STREAM)
serverSocket.connect((IP_addr,2907))

Message2send = "Message from client"
serverSocket.send(Message2send.encode())