import socket

DISCONNECT_MSG = "!DISCONNECT!"
#Format to decode by
FORMAT = 'utf-8'
#Establish byte length 
HEADER = 64
#PORT TO HOST SERVER ON
PORT = 10001
#SERVER ADDRESS TO CONNECT TO
SERVER = "129.21.253.164"
#Convert SERVER and PORT to a tuple
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Initialize socket
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT) #encode the message into bytes
    msg_len = len(message) #get the length of the message in bytes
    send_len = str(msg_len).encode(FORMAT) #encode that length into bytes
    send_len += b' ' * (HEADER-len(send_len)) #64 - length of the header to make the bytes of the string = 64
    client.send(send_len) #send the length of the message in bytes
    client.send(message) #finally, send the message
    print(client.recv(2048).decode(FORMAT))

msg = input("What would you like to send: ")
while msg != DISCONNECT_MSG:
    send(msg)
    msg = input("What would you like to send: ")
send(DISCONNECT_MSG)
