import socket
import pickle
import time
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 65535))
s.listen(1)
#create and bind sockets

class student:
    def __init__(self, id, grade,name):
     self.id = id
     self.grade = grade  
     self.name = name


client, address = s.accept()
#adress - ip adress, client - another socket object

print("Connection has been established")

#welcome message
msg = 'Hello welcome to server......'
client.send(msg.encode("utf-8"))

time.sleep(2)
#created an student object 
alice = student(1, 'A', "Alice")

size = sys.getsizeof(alice)
client.send(pickle.dumps(size))

#send in normal conditions
# data = pickle.dumps(alice)
# client.send(data)

#////////////////////////////////////////

#to get timeout scenario
# time.sleep(5)
# data = pickle.dumps(alice)
# client.send(data)

client.close()