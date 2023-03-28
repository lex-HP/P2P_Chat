from socket import *

def main():
    IP = None
    if IP == None:
        IP=server()
    else:
        client(IP)


def client(IP):
    pass

def server():
    print("starting server")
    serverSocket =  socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('',2907))
    serverSocket.listen(1)

    while True:
        connectionSocket, addr = serverSocket.accept()
        try: 
            message_rcv = connectionSocket.recv(1024).decode()
            print(message_rcv)

            message2send = "Hello"
            message_send = connectionSocket.send(message2send.encode())
            print(message_send)
            connectionSocket.close()
        
        except IOError:
            connectionSocket.send("server unreachable".encode())


    return IP

if __name__ == "__main__":
    main()