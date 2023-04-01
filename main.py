from socket import *
import threading
import datetime

class Chat:
    def __init__(self):
       # self.User1_IP_addr = gethostbyname_ex(gethostname())[2][-1]
        self.User1_IP_addr = ""
        #print("Your IP address is: ", self.User1_IP_addr)
        self.User2Socket = socket(AF_INET, SOCK_STREAM)
        self.User1Socket = socket(AF_INET, SOCK_STREAM)
        self.username = "Alex"
        self.GlobalFlag = False
        # self.User2_IP_addr = ""

    def receiving(self):
        self.User1Socket.bind((self.User1_IP_addr, self.Port))
        self.User1Socket.listen(1)

        print("Waiting for connection...")
        connectionSocket, addr = self.User1Socket.accept()
        print("Connected to", addr, "\n>")

        # Start receiving messages
        while not self.GlobalFlag:
            try:
                message = connectionSocket.recv(1024)
                content_received = message.decode()
                
             #   time_received, username_received ,content_received = received.split("#<>}")

                if content_received == "Goodbye":
                    print("Closing connection socket.")
                    self.GlobalFlag = True
                    connectionSocket.close()
                    raise OSError("Goodbye")
                    return
                #elif message:
                    #print("[" + time_received + "] " + username_received + " > " + content_received + "\n>")
            
            except error:
                print("User has left")
                connectionSocket.close()
                self.GlobalFlag = True
                return

    def sending(self, message=None):
        try:
            self.User2Socket.connect((self.User2_IP_addr, self.Port))
        except:
            pass
        
        print(message)
        # Send message
        try: 
            while not self.GlobalFlag:
                #message = input("> ")
                self.User2Socket.send(str(datetime.datetime.now().strftime("%H:%M:%S") + "#<>}" + self.username + "#<>}" + message).encode())
                if (message == "Goodbye"):
                    self.User2Socket.close()
                    self.GlobalFlag = True
                    print("Connection Closed")
                    raise OSError("Goodbye")
                    return
        except:
            #print("User has left.")
            pass
            return
        
        return
                

    def start_chat(self, User2_IP_addr):
        self.User2_IP_addr = User2_IP_addr
        self.User1_IP_addr = gethostbyname_ex(gethostname())[2][-1]
        #self.User2_IP_addr = input("Enter IP address of User2: ")
        self.Port = 2909
        self.User2Socket = socket(AF_INET, SOCK_STREAM)
        self.User1Socket = socket(AF_INET, SOCK_STREAM)

        #rcv = threading.Thread(target=self.receiving, name="rcv")
        #send = threading.Thread(target=self.sending, name="send")
        #rcv.start()
        #send.start()

        #rcv.join()
        #send.join()
        
# if __name__ == "__main__":
#     try:
#         chat = Chat()
#         chat.start_chat()
#     except:
#         print("ok goodbye")
#         exit()