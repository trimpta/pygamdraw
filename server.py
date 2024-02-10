import socket
import pickle
import threading
import os

host,port = 'localhost', 5555

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.settimeout(500)
server.listen()
print('listening...')

players = {}
id = 0

def handleClient(conn,id):
    while True:
        try:
            point = conn.recv(4096)
            unPoint = pickle.loads(point)
        except Exception as e:
            print(f"Error from {id}: {e}")
            continue
        
        if unPoint == 'stop':
            conn.close
            print("Disconnected")
            break

        for i in players:
            players[i][1].append(unPoint)

        conn.send(pickle.dumps(players[id][1]))
        print(f"id {id}, data {players[id][1]}")
        players[id][1] = []


while True:
    conn,addr = server.accept()
    players[id] = [(conn,addr),[]]
    print(f"{id} IP : {addr}")

    thread = threading.Thread(target=handleClient,args=(conn,id))  
    thread.start()
    id +=1


