import socket, threading, subprocess
from datetime import datetime

#Path to logfile
LOGFILE = "CLIENTLOG.txt"
#Message for user to send to disconnect from server
DISCONNECT_MSG = "!DISCONNECT!"
#Format to decode by
FORMAT = 'utf-8'
#Establish byte length 
HEADER = 64
#PORT TO HOST SERVER ON
PORT = 10003
#SERVER ADDRESS (can put ip address OR use socket to pull ip from hostname)
# IP = socket.gethostbyname(socket.gethostname())
IP = "127.0.0.1"
#Turn IP and port into tuple to pass into socket
ADDR = (IP,PORT)
#initialize the socket with the family of AF_INET and SOCK_STREAM and bind it to an address
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def client_connection(conn,addr):
    print(f"[SERVER] NEW CONNECTION: {addr} connected. \n")

    connected = True 
    while connected: #While the client is connected to the server
        msg_len = conn.recv(HEADER).decode(FORMAT) #How long is the message
        if msg_len:
            msg_len = int(msg_len) #Convert into int
            msg = conn.recv(msg_len).decode(FORMAT) #Recieve message
            if msg == DISCONNECT_MSG: #If the client wants to end the socket, close the connection.
                connected = False
                print(f"[{addr[0]}:{addr[1]}] Disconnected.")
                conn.send("Disconnect Received. Goodbye!".encode(FORMAT))
                print(f"[SERVER] ACTIVE CONNECTIONS: {threading.activeCount() - 2}") #Print how many active connections there are
                
            else:
                output = subprocess.run(msg, shell=True,capture_output=True,text=True) #run the command
                # print(output.stdout)
                print(f"[{addr[0]}:{addr[1]}] \"{msg}\"") #print the command that the user ran
                write_to_file(msg,addr[0]) #write command to file
                # conn.send("Message Received".encode(FORMAT)) 
                conn.send(output.stdout.encode(FORMAT)) #send back the result
    conn.close() #Close connection
        
def start():
    server.listen() #Listen for new connections
    print(f"[SERVER] Server is listening on {IP}:{PORT}")
    while True:
        conn, addr = server.accept() #Waits for new connection. When new connection occurs, store the IP and port to send data back to the address.
        thread = threading.Thread(target=client_connection,args=(conn,addr)) #Pass the connection to client_connection to a new thread
        thread.start() #Start new thread
        print(f"[SERVER] ACTIVE CONNECTIONS: {threading.activeCount() - 1}") #Print how many active connections there are

def write_to_file(msg,sender):
    hostname = socket.gethostname()
    currentTime = datetime.now()
    with open(LOGFILE,"a") as file:
        file.write(f"[{sender} @ {hostname} @ {currentTime}] - {msg} \n")

if __name__ == "__main__":
    print("[SERVER] Sever is starting...")
    start()