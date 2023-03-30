from socket import *

User1_Port = 2907
User2_Port = 2908
User1_IP_addr = gethostbyname(gethostname())
User2Socket = socket(AF_INET, SOCK_STREAM)
User1Socket = socket(AF_INET, SOCK_STREAM)

def main():
    User1Socket.bind((User1_IP_addr, User1_Port))
    User1Socket.listen(1)

    print("Waiting for connection...")
    connectionSocket, addr = User1Socket.accept()
    print("Connected to", addr)

# Start receiving messages
    while True:
        try:
            message = connectionSocket.recv(1024)
            if message:
                print("Received message:", message.decode())
        except error:
            print("Error receiving message:", error)


def sending():
    User2_IP_addr = input("Enter IP address of User2: ")
    User2_IP_addr = gethostbyname(gethostname())



if __name__ == "__main__":
    main()