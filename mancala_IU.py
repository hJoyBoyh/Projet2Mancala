import pygame
from Puit import Puit
from Mancala import Mancala

# init the pygame
pygame.init()

mancala = Mancala()
#size de la fenetre
screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Mancala")

#mancala background

background = pygame.image.load('images/board.jpg')
backgroundX = 120
backgroundY = 200

# test array
#scoreFont
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)

textX = 10
textY = 10


def show_grille():
     
    
    #JOUEUR
    grilleA= font.render(str(mancala.grille.get("A")),True,(0,0,0))
    grilleB= font.render(str(mancala.grille.get("B")),True,(0,0,0))
    grilleC= font.render(str(mancala.grille.get("C")),True,(0,0,0))
    grilleD= font.render(str(mancala.grille.get("D")),True,(0,0,0))
    grilleE= font.render(str(mancala.grille.get("E")),True,(0,0,0))
    grilleF= font.render(str(mancala.grille.get("F")),True,(0,0,0))
    grille2= font.render(str(mancala.grille.get("2")),True,(0,0,0))

    screen.blit(grilleA,(207,285))
    screen.blit(grilleB,(265,285))
    screen.blit(grilleC,(325,285))
    screen.blit(grilleD,(423,285))
    screen.blit(grilleE,(483,285))
    screen.blit(grilleF,(543,285))
    screen.blit(grille2,(600,255))
    #AI
    grilleG= font.render(str(mancala.grille.get("G")),True,(0,0,0))
    grilleH= font.render(str(mancala.grille.get("H")),True,(0,0,0))
    grilleI= font.render(str(mancala.grille.get("I")),True,(0,0,0))
    grilleJ= font.render(str(mancala.grille.get("J")),True,(0,0,0))
    grilleK= font.render(str(mancala.grille.get("K")),True,(0,0,0))
    grilleL= font.render(str(mancala.grille.get("L")),True,(0,0,0))
    grille1= font.render(str(mancala.grille.get("1")),True,(0,0,0))

    screen.blit(grilleG,(207,220))
    screen.blit(grilleH,(265,220))
    screen.blit(grilleI,(325,220))
    screen.blit(grilleJ,(423,220))
    screen.blit(grilleK,(483,220))
    screen.blit(grilleL,(543,220))
    screen.blit(grille1,(145,255))

def show_score(x,y):
    score = font.render("Score: "+ str(score_value),True,(0,0,0))
    screen.blit(score,(x,y))


puits = []
puits.append(Puit("A", 562, 308, 4))
puits.append(Puit("B", 562, 308, 4))
puits.append(Puit("C", 562, 308, 4))
puits.append(Puit("D", 562, 308, 4))
puits.append(Puit("E", 562, 308, 4))
puits.append(Puit("F", 562, 308, 4))
puits.append(Puit("2", 562, 308, 0))
puits.append(Puit("L", 562, 308, 4))
puits.append(Puit("K", 562, 308, 4))
puits.append(Puit("J", 562, 308, 4))
puits.append(Puit("I", 562, 308, 4))
puits.append(Puit("H", 562, 308, 4))
puits.append(Puit("G", 562, 308, 4))
puits.append(Puit("1", 562, 308, 0))

#def show_puit(x,y):
  # puits[0] = font.render(str(puits[0].nbGraines),True,(0,0,0))
   #screen.blit(puits[0],(x,y))

#   
def is_over(rect, pos):
    # function takes a tuple of (x, y) coords and a pygame.Rect object
    # returns True if the given rect overlaps the given coords
    # else it returns False
    return True if rect.collidepoint(pos[0], pos[1]) else False




rectangles = []
def puit_collider(x,y):
    rect_width = 40
    rect_height = 40
    rectangle = pygame.Rect(x,y,rect_width, rect_height)
    #put rectangle in list
    rectangles.append(rectangle)
    # draw the rectangle

    box = pygame.Surface(rectangle.size,pygame.SRCALPHA)
    #box.fill((100,100,100,128))                         # notice the alpha value in the color
    pygame.draw.rect(box,0,box.get_rect())
    screen.blit(box, (x,y))



running = True
while running:
    
# mettre le background en blanc
    screen.fill((255,255,255))

# mettre le board dans screen
    screen.blit(background,(backgroundX,backgroundY))
#mettre les box collider des puits
#JOUEUR
    puit_collider(207,285)
    puit_collider(265,285)
    puit_collider(325,285)
    puit_collider(423,285)
    puit_collider(483,285)
    puit_collider(543,285)
    puit_collider(600,255)
#IA
    puit_collider(207,220)
    puit_collider(265,220)
    puit_collider(325,220)
    puit_collider(423,220)
    puit_collider(483,220)
    puit_collider(543,220)
    puit_collider(145,255)

    show_grille()
    for event in pygame.event.get():
# event fermer window
        if event.type == pygame.QUIT:
            running = False
#event click mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos # recup la position de la souris

            for index, key in enumerate(mancala.grille):
             
             if is_over(rectangles[index], pos):
                 print('The mouse is over the rectangle')
                 mancala.joueurDeplacement(key)
             """
            if is_over(rectangles[0], pos): # pass in the pygame.Rect and the mouse coords
                print('The mouse is over the rectangle')
             
                mancala.joueurDeplacement("A")
               
                
            elif is_over(rectangles[1], pos):
                print('The mouse is over the rectangle')
                mancala.joueurDeplacement("B")
               
            elif is_over(rectangles[2], pos):
                print('The mouse is over the rectangle')
                mancala.joueurDeplacement("C")
            elif is_over(rectangles[3], pos):
                print('The mouse is over the rectangle')
                mancala.joueurDeplacement("D")
            elif is_over(rectangles[4], pos):
                print('The mouse is over the rectangle')
                mancala.joueurDeplacement("E")
            elif is_over(rectangles[5], pos):
                print('The mouse is over the rectangle')  
                mancala.joueurDeplacement("F")  
            else:
                print('The mouse is not over the rectangle')
                print(pos)
            """
           
            


    mancala.ordiDeplacement("random")
        
    show_score(textX,textY)
   # show_puit(puits[0].x, puits[0].y)
    pygame.display.update()