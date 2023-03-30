from socket import *
import threading
import datetime

Port = 2909
User1_IP_addr = gethostbyname(gethostname())
User2Socket = socket(AF_INET, SOCK_STREAM)
User1Socket = socket(AF_INET, SOCK_STREAM)

def receiving():
    User1Socket.bind((User1_IP_addr, Port))
    User1Socket.listen(1)

    print("Waiting for connection...")
    connectionSocket, addr = User1Socket.accept()
    print("Connected to", addr)

# Start receiving messages
    while True:
        try:
            message = connectionSocket.recv(1024)
            if message.decode() == "Goodbye":
                print("Closing connection socket.")
                connectionSocket.close()
                exit()
            elif message:
                print("Received message:", message.decode())
        except error:
            print("Error receiving message:", error)


def sending():
    #User2_IP_addr = gethostbyname(gethostname())

    User2Socket.connect((User2_IP_addr, Port))

    # Send message
    while True:
        message = input("Enter message to send: ")
        User2Socket.send((str(datetime.datetime.now()) + message).encode())
        if (message == "Goodbye"):
            User2Socket.close()
            exit()





if __name__ == "__main__":
    User2_IP_addr = input("Enter IP address of User2: ")
    threading.Thread(target=receiving).start()
    threading.Thread(target=sending).start()


    """
    choice = input("Enter 'send' or 'receive': ")
    if choice == "send":
        sending()
    elif choice == "receive":
        receiving()
    else:
        print("Invalid choice")
    """