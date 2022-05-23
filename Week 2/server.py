import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('10.0.2.15', 50000))
s.listen(1)

client, address = s.accept()
#adress - ip adress, client - another socket object

print("Connection has been established")

#send message
msg = 'Hello welcome to server......'
client.send(msg.encode("utf-8"))

#recieve messsage
msg = client.recv(1024)
print(msg.decode("utf-8"))

client.close()