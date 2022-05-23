import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET Corresponds to IVP4 and SOCK_STREM corresponds to TCP
s.connect((socket.gethostname(), 65535))

# Receive msg
msg = s.recv(1024)
# 1024 is buffer size
print(msg.decode("utf-8"))

# Send msg

msg = 'Hey there bye......'
s.send(msg.encode("utf-8"))

s.close()