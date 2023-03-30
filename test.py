from socket import *
import datetime
User1_IP_addr = gethostbyname_ex("Jonathan")
print(User1_IP_addr[2][0])

print(str(datetime.datetime.now()))