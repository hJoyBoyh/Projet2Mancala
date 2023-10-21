import pygame

# init the pygame
pygame.init()

#size de la fenetre
screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Mancala")

#mancala background

background = pygame.image.load('images/board.jpg')
backgroundX = 110
backgroundY = 400


running = True
while running:
   
    screen.blit(background,(backgroundX,backgroundY))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    pygame.display.update()