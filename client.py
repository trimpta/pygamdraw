import pygame
import pickle
from pablo import netWorker

pygame.init()
screen = pygame.display.set_mode((300,300))
worker = netWorker()


radius = 20
while True:
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("Quitting...")
            worker.s.send(pickle.dumps('stop'))
            pygame.quit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                worker.clear()
        
        if event.type == pygame.MOUSEWHEEL:
            radius += event.y
            radius = 1 if radius<1 else radius
            print('radius set to ', radius)


    if pygame.mouse.get_pressed()[0]:
        worker.send(radius=radius)
    else:
        worker.null()

    worker.drawpoints(screen)
    pygame.display.update()

# god save me