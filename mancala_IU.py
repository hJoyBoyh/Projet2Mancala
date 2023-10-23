import pygame
from Puit import Puit
from Mancala import Mancala

# init the pygame
pygame.init()

mancala = Mancala()


#size de la fenetre
screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Mancala")

# img load
point0 = pygame.image.load("images/e.jpg")
point1 = pygame.image.load("images/1.jpg")
point2 = pygame.image.load("images/2.jpg")
point3 = pygame.image.load("images/3.jpg")
point4 = pygame.image.load("images/4.jpg")
point5 = pygame.image.load("images/5.jpg")
pointFull = pygame.image.load("images/m.jpg")

panier0 = pygame.image.load("images/se.jpg")
panier1 = pygame.image.load("images/s1.jpg")
panier2 = pygame.image.load("images/s2.jpg")
panier3 = pygame.image.load("images/s3.jpg")
panier4 = pygame.image.load("images/s4.jpg")
panier5 = pygame.image.load("images/s5.jpg")
panierFull = pygame.image.load("images/sm.jpg")

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

"""
puits = []
puits.append(Puit("A", 562, 308, 4,("./image/1.jpg")))
puits.append(Puit("B", 562, 308, 4 ,("./image/1.jpg")))
puits.append(Puit("C", 562, 308, 4 ,("./image/1.jpg")))
puits.append(Puit("D", 562, 308, 4 ,("./image/1.jpg")))
puits.append(Puit("E", 562, 308, 4 ,("./image/1.jpg")))
puits.append(Puit("F", 562, 308, 4 ,("./image/1.jpg")))
puits.append(Puit("2", 562, 308, 0 ,("./image/1.jpg")))
puits.append(Puit("L", 562, 308, 4 ,("./image/1.jpg")))
puits.append(Puit("K", 562, 308, 4 ,("./image/1.jpg")))
puits.append(Puit("J", 562, 308, 4 ,("./image/1.jpg")))
puits.append(Puit("I", 562, 308, 4 ,("./image/1.jpg")))
puits.append(Puit("H", 562, 308, 4 ,("./image/1.jpg")))
puits.append(Puit("G", 562, 308, 4 ,("./image/1.jpg")))
puits.append(Puit("1", 562, 308, 0 ,("./image/1.jpg")))
"""
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



# mancala function
gameOver = False

def event_AI():
    mancala.ordiDeplacement("max")
    updateGrill()

def gameOverCheck():
    global gameOver
    print(gameOver)
    if mancala.terminateGame() and gameOver != True:
        gameOver = True
        updateGrill()
        return True
    return False

def orderManager():
    if gameOverCheck() or gameOver:
        evaluation = mancala.evaluate(mancala.grille)
        #print(evaluation)
        if evaluation > 0:
            print("Le joueur a gagne")
            print("Winner player")
        elif evaluation == 0:
            print("Egal")
            print("Winner egal")
        elif evaluation < 0:
            print("AI a gagne")
            print("Winner AI")
    elif mancala.joueurTour:
        print("Tour du joueur")
    else:
        print("Tour du AI")
        event_AI()

def updateGrill():
    orderManager()


def event_puit(id):
    if mancala.joueurDeplacement(puits[id].label) != False:
        updateGrill()
    else:
        orderManager()

def event_reset():
    global gameOver
    global mancala
    mancala = Mancala()
    updateGrill()
    gameOver = False


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


   
    orderManager()
    screen.blit(point1,(300,300))
    show_score(textX,textY)
   # show_puit(puits[0].x, puits[0].y)
    pygame.display.update()