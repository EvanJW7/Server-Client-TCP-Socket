import socket
print("Waiting for client...")
"""Define a socket object. A socket is just an endpoint that receives data that sits at 
an IP address of a port"""
        #socket family type (ipv4), type of socket, so this is a streaming socket(TCP)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind the socket to the machine's server at specific port 
s.bind((socket.gethostname(), 1234))

#Listen. Queue of 5 connections total
s.listen(5)
#Listen forever
while True:
    #Accept
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established. Congratulations.")
    #Send information to the client socket
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    #Close
    clientsocket.close()
