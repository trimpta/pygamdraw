import socket
import pickle
import threading
import sys

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
            point = conn.recv(1024)
            unPoint = pickle.loads(point)
        except Exception as e:
            print(f"disconnecting {id}: {e}")
            conn.close
            break
        

        if unPoint == 'stop':
            conn.close
            players.pop(id)
            print("Disconnected")
            break


        for i in players:
            players[i][1].append(unPoint)
        
        data = pickle.dumps(players[id][1])
        conn.send(len(data))
        conn.send(data)
        print(f"id {id}, data {players[id][1]}")
        players[id][1] = []


while True:
    conn,addr = server.accept()
    players[id] = [(conn,addr),[]]
    print(f"{id} IP : {addr}")

    thread = threading.Thread(target=handleClient,args=(conn,id))  
    thread.start()
    id +=1


