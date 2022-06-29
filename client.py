import socket
#Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect
s.connect((socket.gethostname(), 1234))

#Receive
msg = s.recv(1024)
print(msg.decode("utf-8"))
