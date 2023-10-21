import pygame

# init the pygame
pygame.init()

#size de la fenetre
screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Mancala")

#mancala background

background = pygame.image.load('images/board.jpg')
backgroundX = 120
backgroundY = 200



running = True
while running:
   
    screen.blit(background,(backgroundX,backgroundY))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            print(mouse_x)
            print(mouse_y)

            print("Mouse button pressed")
    

    pygame.display.update()