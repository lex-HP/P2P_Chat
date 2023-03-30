from socket import *
import threading
import datetime

class Chat:
    def __init__(self):
        self.Port = 2909
        self.User1_IP_addr = gethostbyname_ex(gethostname())[2][-1]
        print("Your IP address is: ", self.User1_IP_addr)
        self.User2Socket = socket(AF_INET, SOCK_STREAM)
        self.User1Socket = socket(AF_INET, SOCK_STREAM)
        self.username = "Alex"
        self.GlobalFlag = False

    def receiving(self):
        self.User1Socket.bind((self.User1_IP_addr, self.Port))
        self.User1Socket.listen(1)

        print("Waiting for connection...")
        connectionSocket, addr = self.User1Socket.accept()
        print("Connected to", addr, "\n>")

        # Start receiving messages
        while not self.GlobalFlag:
            if self.GlobalFlag:
                break
            try:
                message = connectionSocket.recv(1024)
                received = message.decode()
                time_received, username_received ,content_received = received.split("#<>}")

                if content_received == "Goodbye":
                    print("Closing connection socket.")
                    self.GlobalFlag = True
                    connectionSocket.close()
                    raise OSError("Connection Closed - Goodbye")
                elif message:
                    print("[" + time_received + "] " + username_received + " > " + content_received + "\n>")
            except error:
                print("User has left")
                connectionSocket.close()
                self.GlobalFlag = True
                break 

    def sending(self):
        self.User2Socket.connect((self.User2_IP_addr, self.Port))
        # Send message 
        while not self.GlobalFlag:
            message = input("> ")
            self.User2Socket.send(str(datetime.datetime.now().strftime("%H:%M:%S") + "#<>}" + self.username + "#<>}" + message).encode())
            if (message == "Goodbye"):
                self.User2Socket.close()
                self.GlobalFlag = True
                print("Connection Closed")
                raise OSError("Connection closed - Goodbye")
        print("User has left.")
        exit()
                

    def start_chat(self):
        self.User2_IP_addr = input("Enter IP address of User2: ")
        rcv = threading.Thread(target=self.receiving, name="rcv")
        send = threading.Thread(target=self.sending, name="send")
        rcv.start()
        send.start()

        rcv.join()
        send.join()
        exit()
        
if __name__ == "__main__":
    chat = Chat()
    try: 
        chat.start_chat()
    except: 
        exit()