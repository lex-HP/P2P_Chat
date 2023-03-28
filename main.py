from socket import *

IP_addr = "192.168.56.1"

def main():
    IP = None
    if IP == None:
        IP=server()
    else:
        client(IP)


def client(connectionSocket, addr):
    connectionSocket.send("Hello".encode())
    while True:
        try: 
            message = connectionSocket.recv(1024)
            if message:
                print(message)
        except:
            continue
    

def server():
    print("starting server")
    serverSocket =  socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((IP_addr,2907))
    serverSocket.listen(1)

    safety = 0
    while safety <= 100:
        safety = safety + 1 

        connectionSocket, addr = serverSocket.accept()
        try: 
            client(connectionSocket, addr)
        except IOError:
            connectionSocket.send("server unreachable".encode())


if __name__ == "__main__":
    main()