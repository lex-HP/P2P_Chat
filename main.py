from tkinter import *
from tkinter import filedialog
from socket import *
from threading import Thread
from datetime import datetime
import pandas as pd

class ChatGUI:
    def __init__(self):
        self.df = pd.DataFrame(columns=['Username', 'Timestamp', 'Message'])
        self.window = Tk()
        self.window.title("Chat Program")
        self.create_widgets()

        
    def bExport(self):
        self.df.to_csv('chatlog.csv', encoding='utf-8', index=False)



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

        # Create send message field and button
        self.send_message_input = Entry(self.window, width=40)
        self.send_message_input.grid(row=4, column=0, padx=5, pady=5)
        self.send_message_button = Button(self.window, text="Send", command=self.send_message)
        self.send_message_button.grid(row=4, column=1, padx=5, pady=5)


        self.export_button = Button(self.window, text="Export to CSV", command=self.bExport)
        self.export_button.grid(row=1, column=1)



    def start(self):
        self.window.mainloop()

    def send_message(self):
        timestamp = datetime.now()
        message = self.send_message_input.get()
        self.update_chat_log(message, "You")
        self.send_message_input.delete(0, END)


        # Send message to User2
        user2_ip = self.user2_ip_input.get()
        user2_port = 5000
        with socket(AF_INET, SOCK_STREAM) as sock:
            sock.connect((user2_ip, user2_port))
            sock.sendall(message.encode())
        
        

    def update_chat_log(self, message, user):
        self.chat_log.config(state=NORMAL)
        self.chat_log.insert(END, user + ": " + message + "\n")
        self.chat_log.config(state=DISABLED)

        timestamp = datetime.now()
        existing_row = self.df[self.df['Timestamp'] == timestamp]
        if not existing_row.empty:
            # update existing row with new message content
            self.df.loc[existing_row.index[0], 'Message'] = message
        else:
            # append new row with message content and timestamp
            self.df = self.df._append({'Username': user, 'Timestamp': timestamp, 'Message': message}, ignore_index=True)         

def listen_for_messages(ip, port, chat_gui):
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.bind((ip, port))
        sock.listen()
        while True:
            conn, addr = sock.accept()
            with conn:
                data = conn.recv(1024)
                if not data:
                    break
                message = data.decode()
                chat_gui.update_chat_log(message, "Server")

if __name__ == '__main__':
    chat_gui = ChatGUI()

    ip = gethostbyname_ex(gethostname())[2][-1]
    port = 5000
    listener_thread = Thread(target=listen_for_messages, args=(ip, port, chat_gui))
    listener_thread.start()

    chat_gui.start()