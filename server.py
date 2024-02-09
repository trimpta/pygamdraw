import socket
import pickle
import threading
import os

host,port = 'localhost', 5555

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()
print('listening...')

players = []

def handleClient(conn,addr):
    while True:

        point = conn.recv(100)
        print(pickle.loads(point))

        for player,addr in players:
            player.send(point)
            print('send to:', addr)

while True:
    conn,addr = server.accept()
    players.append((conn,addr))
    print(f"IP : {addr}")

    thread = threading.Thread(target=handleClient,args=(conn,addr))  
    thread.start()  


