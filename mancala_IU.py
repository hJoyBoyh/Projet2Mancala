import pygame
from Puit import Puit
from Mancala import Mancala

# init the pygame
pygame.init()


#size de la fenetre
screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Mancala")



#mancala background

background = pygame.image.load('images/board.jpg')
backgroundX = 120
backgroundY = 200


# mancala block
mancala = Mancala()
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


font = pygame.font.Font('freesansbold.ttf',32)

tourX = 10
tourY = 10
def show_tour():
    tour_value = ""
    if mancala.joueurTour:
        tour_value = "Tour du Joueur"
    else:
        tour_value = "Tour du AI"

    score = font.render(tour_value,True,(0,0,0))
    screen.blit(score,(tourX,tourY))

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


# instancier puits
puits = []
puits.append(Puit("A", 198,280, 4,("images/4.jpg")))
puits.append(Puit("B", 259,280, 4 ,("images/4.jpg")))
puits.append(Puit("C", 319,280, 4 ,("images/4.jpg")))
puits.append(Puit("D", 417, 280, 4 ,("images/4.jpg")))
puits.append(Puit("E", 478, 280, 4 ,("images/4.jpg")))
puits.append(Puit("F", 536, 280, 4 ,("images/4.jpg")))
puits.append(Puit("2", 595, 210, 0 ,("images/se.jpg")))
puits.append(Puit("L", 198, 210, 4 ,("images/4.jpg")))
puits.append(Puit("K", 259, 210, 4 ,("images/4.jpg")))
puits.append(Puit("J", 319, 210, 4 ,("images/4.jpg")))
puits.append(Puit("I", 417, 210, 4 ,("images/4.jpg")))
puits.append(Puit("H", 478, 210, 4 ,("images/4.jpg")))
puits.append(Puit("G", 536, 210, 4 ,("images/4.jpg")))
puits.append(Puit("1", 140, 210, 0 ,("images/se.jpg")))


# change son nbGraines et son image correspondant
def update_puits():
   for index, key in enumerate(mancala.grille):
      puits[index].nbGraines = mancala.grille.get(puits[index].label)

    #basket et puit si = 0
      if not puits[index].label in "12" and  puits[index].nbGraines == 0:
          puits[index].bouton = pygame.image.load("images/e.jpg")
      if puits[index].label in "12" and  puits[index].nbGraines == 0:
          puits[index].bouton = pygame.image.load("images/se.jpg")
       
    # puit 
      if not puits[index].label in "12" and puits[index].nbGraines == 1:
          puits[index].bouton = pygame.image.load("images/1.jpg")

      if not puits[index].label in "12" and puits[index].nbGraines == 2:
          puits[index].bouton = pygame.image.load("images/2.jpg")

      if not puits[index].label in "12" and  puits[index].nbGraines == 3:
          puits[index].bouton = pygame.image.load("images/3.jpg")

      if not puits[index].label in "12" and  puits[index].nbGraines == 4:
          puits[index].bouton = pygame.image.load("images/4.jpg")

      if not puits[index].label in "12" and puits[index].nbGraines == 5:
          puits[index].bouton = pygame.image.load("images/5.jpg")
    
      if not puits[index].label in "12" and  puits[index].nbGraines > 5:
          puits[index].bouton = pygame.image.load("images/m.jpg")

    # panier
      if puits[index].label in "12" and puits[index].nbGraines == 1:
          puits[index].bouton = pygame.image.load("images/s1.jpg")

      if puits[index].label in "12" and puits[index].nbGraines == 2:
          puits[index].bouton = pygame.image.load("images/s2.jpg")

      if puits[index].label in "12" and  puits[index].nbGraines == 3:
          puits[index].bouton = pygame.image.load("images/s3.jpg")

      if puits[index].label in "12" and  puits[index].nbGraines == 4:
          puits[index].bouton = pygame.image.load("images/s4.jpg")

      if puits[index].label in "12" and puits[index].nbGraines == 5:
          puits[index].bouton = pygame.image.load("images/s5.jpg")
    
      if puits[index].label in "12" and  puits[index].nbGraines > 5:
          puits[index].bouton = pygame.image.load("images/sm.jpg")


# afficher img du puit associer  
def show_puit_img():
    for i in puits:
        screen.blit(i.bouton,(i.x,i.y))

#afficer le nbGraines du puit associer
def show_puit_score():
    
    #JOUEUR
    puitA= font.render(str(puits[0].nbGraines),True,(0,0,0))
    puitB= font.render(str(puits[1].nbGraines),True,(0,0,0))
    puitC= font.render(str(puits[2].nbGraines),True,(0,0,0))
    puitD= font.render(str(puits[3].nbGraines),True,(0,0,0))
    puitE= font.render(str(puits[4].nbGraines),True,(0,0,0))
    puitF= font.render(str(puits[5].nbGraines),True,(0,0,0))
    puit2= font.render(str(puits[6].nbGraines),True,(0,0,0))

    screen.blit(puitA,(207,350))
    screen.blit(puitB,(265,350))
    screen.blit(puitC,(325,350))
    screen.blit(puitD,(423,350))
    screen.blit(puitE,(483,350))
    screen.blit(puitF,(543,350))
    screen.blit(puit2,(700,255))
    #AI
    puitG= font.render(str(puits[7].nbGraines),True,(0,0,0))
    puitH= font.render(str(puits[8].nbGraines),True,(0,0,0))
    puitI= font.render(str(puits[9].nbGraines),True,(0,0,0))
    puitJ= font.render(str(puits[10].nbGraines),True,(0,0,0))
    puitK= font.render(str(puits[11].nbGraines),True,(0,0,0))
    puitL= font.render(str(puits[12].nbGraines),True,(0,0,0))
    puit1= font.render(str(puits[13].nbGraines),True,(0,0,0))

    screen.blit(puitG,(207,170))
    screen.blit(puitH,(265,170))
    screen.blit(puitI,(325,170))
    screen.blit(puitJ,(423,170))
    screen.blit(puitK,(483,170))
    screen.blit(puitL,(543,170))
    screen.blit(puit1,(90,255))

  

#dectection de click   
def click_dectection(rect, pos):
    return True if rect.collidepoint(pos[0], pos[1]) else False

# puit collider create et add dans la listPuitCollider dont les idx son sync avec ceux de mancala.grille et puits
listPuitCollider = []
def puit_collider(x,y):
    rect_width = 40
    rect_height = 40
    rectangle = pygame.Rect(x,y,rect_width, rect_height)

    #append rectangle in list
    listPuitCollider.append(rectangle)

    # dessine le rectangle
    box = pygame.Surface(rectangle.size,pygame.SRCALPHA)
    #box.fill((100,100,100,128))                         # notice the alpha value in the color
    pygame.draw.rect(box,0,box.get_rect())
    screen.blit(box, (x,y))







running = True
while running:
    
# mettre le background en blanc
    screen.fill((255,255,255))

# affiche le board dans screen
    screen.blit(background,(backgroundX,backgroundY))

# affiche les puits
    show_puit_img()
    show_puit_score()
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


    for event in pygame.event.get():

# event fermer window
        if event.type == pygame.QUIT:
            running = False

#event click mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos # recup la position de la souris

            for index, key in enumerate(mancala.grille):
             
             # vu que la listPuitCollider est sync avec la grille et les puits quand tu 
             # click sur un collider avec son index tu prend le puit de la grille qui a le meme index et tu effectue la fonction
             if click_dectection(listPuitCollider[index], pos):
                 print('The mouse is over the rectangle')
                 mancala.joueurDeplacement(key)
                 
                 orderManager()
                 
                 update_puits()

    show_tour()
    
    
   # show_puit(puits[0].x, puits[0].y)
    pygame.display.update()