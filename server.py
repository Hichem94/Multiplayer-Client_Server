import socket
from _thread import *
import sys


server = "172.19.196.199"
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

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(str(tup[0]) + "," + str(tup[1]))


pos = [(0,0), (100,100)]
def threaded_client(conn, player):
    conn.send( str.encode(make_pos( (pos[player]) )) )
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode()) # amount of informations we want to recv
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = make_pos(pos[0])
                else:
                    reply = make_pos(pos[1])
                
                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(str.encode(reply))
        except:
            break
        
    print("Lost connection")
    conn.close()


currentPlayer = 0
while True:
    conn, addr = s.accept() # accept any incomming connections
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1


