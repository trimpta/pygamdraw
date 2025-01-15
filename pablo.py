import socket
import pickle
import pygame
import pickle
from random import randint



class netWorker:
    
    # points = []

    def __init__(self, host:str = 'localhost', port:int = 5555):

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.connect((host, port))
            self.s.settimeout(50)

            print("connected")

        except Exception as e:
            print(e)

        self.bg ='black'
        
    def send(self, color = (255,255,255), radius = 20):
        pos = pygame.mouse.get_pos()
        point = (color, pos, radius)
        self.s.send(pickle.dumps(point))
        print('sent.')

    def drawpoints(self, screen):

        try:
            size = pickle.loads(self.s.recv(1024))
            data = pickle.loads(self.s.recv(size))
        except Exception as e:  
            print(f"Invalid data {e}")
            return

        for i in data:
            if i == 'clear':
                print("cleargot")
                screen.fill(self.bg)
                continue
            elif i == 'c':
                self.clear()
                self.bg = (randint(0,255),randint(0,255),randint(0,255))
                continue
            elif i == '':
                continue
            else:
                color, pos, radius = i
                pygame.draw.circle(screen, color, pos, radius)

    def null(self):
        self.s.send(pickle.dumps(''))

    def clear(self):
        self.s.send(pickle.dumps('clear'))
        print("clearsent")

