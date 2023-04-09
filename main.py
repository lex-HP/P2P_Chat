from socket import *
import threading
import datetime
import time

message = "<><><><><><><><>5<>"
flagSetUser2 = 0


def startChat(ip):
    global Port, User1_IP_addr, User1Socket, User2_IP_addr, username, rcv, send, User2Socket
    User2_IP_addr = ip
    Port = 2910
    User1_IP_addr = gethostbyname_ex(gethostname())[2][-1]
    print("Your IP address is: ", User1_IP_addr)
    User1Socket = socket(AF_INET, SOCK_STREAM)
    username = "Alex"
    #User2_IP_addr = input("Enter IP address of User2: ")
    #User2_IP_addr = "192.168.8.239"
    rcv = threading.Thread(target=receiving, name="rcv")
    send = threading.Thread(target=sending, name="send", args=(message, ))
    
    rcv.start()
    time.sleep(1)
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
            
            print("message = connectionSocket.recv(1024)")
            rcv_message = connectionSocket.recv(1024)
            print("received = message.decode()")
            received = rcv_message.decode()
            print(" time_received, username_received ,content_received = received.")
            time_received, username_received ,content_received = received.split("#<>}")
            

            if content_received == "Goodbye":
                print("Closing connection socket.")
                connectionSocket.close()
                exit()
            elif rcv_message:
                print("[" + time_received + "] " + username_received + " > " + content_received + "\n>")
        except error:
            print("User has left")
            connectionSocket.close()
            exit()


def sending(message):
    # Send message
    User2Socket = socket(AF_INET, SOCK_STREAM)
    User2Socket.connect((User2_IP_addr, Port))
       
    while True:
        #message = input("> ")
        User2Socket.send(str(datetime.datetime.now().strftime("%H:%M:%S") + "#<>}" + username + "#<>}" + message).encode())
        if (message == "Goodbye"):
            User2Socket.close()
            print("Connection Closed")
            exit()


if __name__ == "__main__":
    ip_addr = input("Enter IP address of User2: ")
    startChat(ip_addr)


"""
def sending(message):
    # Send message
    #if User2Socket is None:
    global oldMessage
    oldMessage = ""
    while True:
        if message != oldMessage:
            oldMessage = message
            #message = input("> ")
            if message != "<><><><><><><><>5<>":
                print("message to be sent", message)
                User2Socket.send(str(datetime.datetime.now().strftime("%H:%M:%S") + "#<>}" + username + "#<>}" + message).encode())
                if (message == "Goodbye"):
                    User2Socket.close()
                    print("Connection Closed")
                    exit()
            elif message == "<><><><><><><><>5<>":
                print("creating user2 socket")
                User2Socket = socket(AF_INET, SOCK_STREAM)
                User2Socket.connect((User2_IP_addr, Port))
        else:
            time.sleep(0.3)
        
"""
