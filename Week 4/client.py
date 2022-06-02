import socket
import pickle
from time import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET Corresponds to IVP4 and SOCK_STREM corresponds to TCP

s.connect((socket.gethostname(), 65535))

class student:
    def __init__(self, id, grade,name):
     self.id = id
     self.grade = grade  
     self.name = name


# Receive  welcome msg
msg = s.recv(1024)
# 1024 is buffer size
print(msg.decode("utf-8"))
size = s.recv(1024)
size = pickle.loads(size)

# #Accept data in normal conditions

# data = s.recv(4096)
# data_variable = pickle.loads(data)

# #Print data
# print("name: ", data_variable.name)
# print("id: ", data_variable.id)
# print("grade: ", data_variable.grade)

#////////////////////////////////////////

# Rejection scenario

# if(size > 4): 
#     print("Size exceeded!!! Rejected")
#     s.close()

#////////////////////////////////////////

#Timeout scenario

# s.settimeout(2)
# data = s.recv(4096)
# data_variable = pickle.loads(data)

# #Print data
# print("nam: ", data_variable.name)
# print("id: ", data_variable.id)
# print("grade: ", data_variable.grade)

s.close()