from tkinter import *
from socket import *
from threading import Thread
from main import startChat, sending, message
import main

class ChatGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Chat Program")
        self.create_widgets()

    def bSubmit(self):
        ip_addr = str(self.user2_ip_input.get())
        Thread(target=startChat, args=(ip_addr,)).start()
        #Thread(target=startChat, args=(ip_addr)).start()
    
    def create_widgets(self):
        # Create labels
        Label(self.window, text="Enter IP address of User2:").grid(row=0, column=0, sticky=W)
        Label(self.window, text="Your IP address is: " + gethostbyname_ex(gethostname())[2][-1]).grid(row=1, column=0, sticky=W)
        Label(self.window, text="Chat Log:").grid(row=2, column=0, sticky=W)

        # Create input fields
        self.user2_ip_input = Entry(self.window, width=20)
        self.user2_ip_input.grid(row=0, column=1, padx=5, pady=5)

        # Create chat log 
        self.chat_log = Text(self.window, width=50, height=10, state=DISABLED)
        self.chat_log.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        ip_addr = self.user2_ip_input.get()
        self.ip_submit = Button(self.window,text="Submit IP", command=self.bSubmit)
        self.ip_submit.grid(row=1, column=1)

        # Create send message field and button
        self.send_message_input = Entry(self.window, width=40)
        self.send_message_input.grid(row=4, column=0, padx=5, pady=5)
        self.send_message_button = Button(self.window, text="Send", command=self.send_message)
        self.send_message_button.grid(row=4, column=1, padx=5, pady=5)

    def start(self):
        self.window.mainloop()

    def send_message(self):
        messageBox = self.send_message_input.get()
        self.send_message_input.delete(0, END)
        if messageBox == "Goodbye":
            self.chat_log.config(state=NORMAL)
            self.chat_log.insert(END, "You: " + messageBox + "\n")
            self.chat_log.config(state=DISABLED)
            main.message = messageBox
            #Thread(target=sending, args=(message, )).start()
            self.window.quit()
        else:
            self.chat_log.config(state=NORMAL)
            self.chat_log.insert(END, "You: " + messageBox + "\n")
            self.chat_log.config(state=DISABLED)
            main.message = messageBox
            #sending(message)
            #Thread(target=sending, args=(messageBox, )).start()
            #Thread(target=self.chat.sending(self.send_message_input.get())).start()

    def update_chat_log(self, message):
        self.chat_log.config(state=NORMAL)
        self.chat_log.insert(END, message + "\n")
        self.chat_log.config(state=DISABLED)

    

gui = ChatGUI()
#Thread(target=gui.chat.start_chat).start()

gui.start()
