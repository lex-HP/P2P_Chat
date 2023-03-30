from socket import *

IP_addr = "10.239.229.103"

def main():
    IP = None
    if IP == None:
        IP=server()
    else:
        client(IP)


def client(connectionSocket, addr):
    #connectionSocket.send("Hello".encode())
    while True:
        try: 
            message = connectionSocket.recv(1024)
            if message:
                print(message.decode())
        except:
            continue
    

def server():
    print("starting server")
    serverSocket =  socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((IP_addr,2907))
    serverSocket.listen(1)

    safety = 0
    while True: 
        safety = safety + 1
        if safety >= 100:
            break

        connectionSocket, addr = serverSocket.accept()
        try: 
            client(connectionSocket, addr)
        except IOError:
            connectionSocket.send("server unreachable".encode())


if __name__ == "__main__":
    main()