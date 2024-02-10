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
            self.s.settimeout(500)

            print("connected")

        except Exception as e:
            print(e)

        self.bg ='black'
        
    def send(self, color = (255,255,255), radius = 20):
        pos = pygame.mouse.get_pos()
        point = (color, pos, radius)
        self.s.send(pickle.dumps(point))
        print(pos)

    def drawpoints(self, screen):

        try:
            data = pickle.loads(self.s.recv(1000))
        except pickle.UnpicklingError:
            print("Invalid data recieved")
            return

        if data == 'clear':
            screen.fill(self.bg)

        elif data == 'null':
            return
        else:
            color, pos, radius = data
            pygame.draw.circle(screen, color, pos, radius)
            print('.',end = '')

    def null(self):
        self.s.send(pickle.dumps('null'))

    def clear(self):
        self.s.send(pickle.dumps('clear'))

