import socket
import pickle
# import pygame
# from pablo import netWorker

def testserver():

    host_port = ('localhost', 5555)

    a,b,c = socket.socket(socket.AF_INET, socket.SOCK_STREAM), socket.socket(socket.AF_INET, socket.SOCK_STREAM), socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    a.connect(host_port)
    b.connect(host_port)
    c.connect(host_port)
    print("connected")

    point = pickle.dumps(('white', (69,69), 20)) #color, pos, radius

    a.send(point)
    b.send(point)
    c.send(point)
    print("Points sent")

    print(pickle.loads(a.recv(100)))
    print(pickle.loads(b.recv(100)))
    print(pickle.loads(c.recv(100)))
    print("Points recieved")

testserver()
testserver()
