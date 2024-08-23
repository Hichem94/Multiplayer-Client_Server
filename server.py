import socket
from _thread import *
import sys


server = "192.168.0.69"
port   = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind (server,port) to the socket
try:
    s.bind( (server, port) )
except socket.error as e:
    str(e)

# Listening for connections
s.listen(2) # I only want two people to be able to connect to my server
print("Waiting for connection, Server Started")


def threaded_client(conn):
    
    reply = ""
    while True:
        try:
            data = conn.recv(2048) # amount of informations we want to recv
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending : ", reply)

            conn.sendall(str.encode(reply))
        except:
            break


while True:
    conn, addr = s.accept() # accept any incomming connections
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn,))


