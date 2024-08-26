import socket
from _thread import *
import sys
from player import Player
import pickle

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


players = [Player(0,0,50,50,(255,0,0)), Player(100,100,50,50,(0,0,255))]

def threaded_client(conn, player):
    conn.send( pickle.dumps(players[player]) )
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048)) # amount of informations we want to recv
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                
                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall( pickle.dumps(reply) )
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


