import threading
import datetime
from socket import *

Port = 2909
User1_IP_addr = gethostbyname_ex(gethostname())[2][-1]
print("Your IP address is: ", User1_IP_addr)
User2Socket = socket(AF_INET, SOCK_STREAM)
User1Socket = socket(AF_INET, SOCK_STREAM)
username = "Alex"

# Flag to indicate when the sending thread should terminate
terminate_sending = False

def receiving():
    User1Socket.bind((User1_IP_addr, Port))
    User1Socket.listen(1)

    print("Waiting for connection...")
    connectionSocket, addr = User1Socket.accept()
    print("Connected to", addr, "\n>")

    # Start receiving messages
    while not terminate_sending:
        try:
            message = connectionSocket.recv(1024)
            received = message.decode()
            time_received, username_received ,content_received = received.split("#<>}")
                
            if content_received == "Goodbye":
                print("Closing connection socket.")
                connectionSocket.close()
                # Set flag to terminate sending thread
                global terminate_sending
                terminate_sending = True
                break
            elif message:
                print("[" + time_received + "] " + username_received + " > " + content_received + "\n>")
        except error:
            print("User has left")
            connectionSocket.close()
            # Set flag to terminate sending thread
            terminate_sending = True
            break


def sending():
    global terminate_sending
    User2Socket.connect((User2_IP_addr, Port))
    # Send message
    while not terminate_sending:
        message = input("> ")
        User2Socket.send(str(datetime.datetime.now().strftime("%H:%M:%S") + "#<>}" + username + "#<>}" + message).encode())
        if (message == "Goodbye"):
            User2Socket.close()
            print("Connection Closed")
            # Set flag to terminate sending thread
            terminate_sending = True
            break

if __name__ == "__main__":
    #User2_IP_addr = input("Enter IP address of User2: ")
    User2_IP_addr = "192.168.8.239"
    rcv = threading.Thread(target=receiving, name="rcv")
    send = threading.Thread(target=sending, name="send")
    rcv.start()
    send.start()
    # Wait for both threads to terminate
    rcv.join()
    send.join()
