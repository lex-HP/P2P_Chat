from socket import *
import threading
import datetime

def startChat(ip):
    global Port, User1_IP_addr, User1Socket, User2_IP_addr, username, User2Socket, rcv, send
    User2_IP_addr = ip
    Port = 2910
    User1_IP_addr = gethostbyname_ex(gethostname())[2][-1]
    print("Your IP address is: ", User1_IP_addr)
    User2Socket = socket(AF_INET, SOCK_STREAM)
    User1Socket = socket(AF_INET, SOCK_STREAM)
    User2Socket.connect((User2_IP_addr, Port))
    username = "Alex"
    #User2_IP_addr = input("Enter IP address of User2: ")
    #User2_IP_addr = "192.168.8.239"
    rcv = threading.Thread(target=receiving, name="rcv")
    #send = threading.Thread(target=sending, name="send")
    rcv.start()
    send.start()

    rcv.join()
    send.join()

def receiving():
    User1Socket.bind((User1_IP_addr, Port))
    User1Socket.listen(1)

    print("Waiting for connection...")
    connectionSocket, addr = User1Socket.accept()
    print("Connected to", addr, "\n>")

# Start receiving messages
    while True:
        try:
            message = connectionSocket.recv(1024)
            received = message.decode()
            time_received, username_received ,content_received = received.split("#<>}")
                
            if content_received == "Goodbye":
                print("Closing connection socket.")
                connectionSocket.close()
                exit()
            elif message:
                print("[" + time_received + "] " + username_received + " > " + content_received + "\n>")
        except error:
            print("User has left")
            connectionSocket.close()
            exit()


def sending(message):
    # Send message
    while True:
        #message = input("> ")
        User2Socket.send(str(datetime.datetime.now().strftime("%H:%M:%S") + "#<>}" + username + "#<>}" + message).encode())
        if (message == "Goodbye"):
            User2Socket.close()
            print("Connection Closed")
            exit()
    


if __name__ == "__main__":
    startChat()
