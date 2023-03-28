from socket import *

IP_addr = "192.168.56.1"
serverSocket =  socket(AF_INET, SOCK_STREAM)
serverSocket.connect((IP_addr,2907))

serverSocket.send("test".encode())