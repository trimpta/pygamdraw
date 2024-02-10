import socket
import pickle
import pygame
import pickle



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
            data = pickle.loads(self.s.recv(4096))
        except Exception as e:
            print(f"Invalid data {e}")
            return

        for i in data:
            if i == 'clear':
                screen.fill(self.bg)
            elif i == 'null':
                continue
            else:
                color, pos, radius = i
                pygame.draw.circle(screen, color, pos, radius)

    def null(self):
        self.s.send(pickle.dumps('null'))

    def clear(self):
        self.s.send(pickle.dumps('clear'))

