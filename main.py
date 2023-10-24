import pygame
from Puit import Puit
from Mancala import Mancala
from mancala_IU import Mancala_UI

# init the pygame
pygame.init()


#size de la fenetre
screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Mancala")

#global variable
gameOver = False
#instance mancala 
mancala = Mancala()

# detection click bouton
def click_dectection(rect, pos):
    return True if rect.collidepoint(pos[0], pos[1]) else False

def play():

    #mancala board
    board = pygame.image.load('images/board.jpg')
    boardX = 120
    boardY = 200
    #-------------------

    # afficher tour de quel participant
    
    font = pygame.font.Font('freesansbold.ttf',32)
    tourX = 10
    tourY = 10
    
    
    def show_tour(tour_value):

        score = font.render(tour_value,True,(0,0,0))
        screen.blit(score,(tourX,tourY))
        

       

#-------------------


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
            
             show_tour("Winner player")
            elif evaluation == 0:
                show_tour("Egal")
                print("Winner egal")
            elif evaluation < 0:
                print("AI a gagne")
                show_tour("Winner AI")
         elif mancala.joueurTour:
            print("Tour du joueur")
            show_tour("Tour du Joueur")
         else:
            print("Tour du AI")
            show_tour("Tour du AI")
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
    mancala_UI =  Mancala_UI()

    # change son nbGraines et son image correspondant
    def update_puits():
        for index, key in enumerate(mancala.grille):
            mancala_UI.puits[index].nbGraines = mancala.grille.get(mancala_UI.puits[index].label)

    #basket et puit si = 0
            if not mancala_UI.puits[index].label in "12" and  mancala_UI.puits[index].nbGraines == 0:
                   mancala_UI.puits[index].bouton = pygame.image.load("images/e.jpg")
            if mancala_UI.puits[index].label in "12" and  mancala_UI.puits[index].nbGraines == 0:
                mancala_UI.puits[index].bouton = pygame.image.load("images/se.jpg")
       
    # puit 
            if not mancala_UI.puits[index].label in "12" and mancala_UI.puits[index].nbGraines == 1:
                mancala_UI.puits[index].bouton = pygame.image.load("images/1.jpg")

            if not mancala_UI.puits[index].label in "12" and mancala_UI.puits[index].nbGraines == 2:
                mancala_UI.puits[index].bouton = pygame.image.load("images/2.jpg")

            if not mancala_UI.puits[index].label in "12" and  mancala_UI.puits[index].nbGraines == 3:
                mancala_UI.puits[index].bouton = pygame.image.load("images/3.jpg")

            if not mancala_UI.puits[index].label in "12" and  mancala_UI.puits[index].nbGraines == 4:
                 mancala_UI.puits[index].bouton = pygame.image.load("images/4.jpg")

            if not mancala_UI.puits[index].label in "12" and mancala_UI.puits[index].nbGraines == 5:
                mancala_UI.puits[index].bouton = pygame.image.load("images/5.jpg")
    
            if not mancala_UI.puits[index].label in "12" and  mancala_UI.puits[index].nbGraines > 5:
                mancala_UI.puits[index].bouton = pygame.image.load("images/m.jpg")

    # panier
            if mancala_UI.puits[index].label in "12" and mancala_UI.puits[index].nbGraines == 1:
                mancala_UI.puits[index].bouton = pygame.image.load("images/s1.jpg")

            if mancala_UI.puits[index].label in "12" and mancala_UI.puits[index].nbGraines == 2:
                mancala_UI.puits[index].bouton = pygame.image.load("images/s2.jpg")

            if mancala_UI.puits[index].label in "12" and  mancala_UI.puits[index].nbGraines == 3:
                mancala_UI.puits[index].bouton = pygame.image.load("images/s3.jpg")

            if mancala_UI.puits[index].label in "12" and  mancala_UI.puits[index].nbGraines == 4:
                mancala_UI.puits[index].bouton = pygame.image.load("images/s4.jpg")

            if mancala_UI.puits[index].label in "12" and mancala_UI.puits[index].nbGraines == 5:
                 mancala_UI.puits[index].bouton = pygame.image.load("images/s5.jpg")
    
            if mancala_UI.puits[index].label in "12" and  mancala_UI.puits[index].nbGraines > 5:
                mancala_UI.puits[index].bouton = pygame.image.load("images/sm.jpg")


    def show_puit_score():
    
    #JOUEUR
        puitA= font.render(str(mancala_UI.puits[0].nbGraines),True,(0,0,0))
        puitB= font.render(str(mancala_UI.puits[1].nbGraines),True,(0,0,0))
        puitC= font.render(str(mancala_UI.puits[2].nbGraines),True,(0,0,0))
        puitD= font.render(str(mancala_UI.puits[3].nbGraines),True,(0,0,0))
        puitE= font.render(str(mancala_UI.puits[4].nbGraines),True,(0,0,0))
        puitF= font.render(str(mancala_UI.puits[5].nbGraines),True,(0,0,0))
        puit2= font.render(str(mancala_UI.puits[6].nbGraines),True,(0,0,0))

        screen.blit(puitA,(207,350))
        screen.blit(puitB,(265,350))
        screen.blit(puitC,(325,350))
        screen.blit(puitD,(423,350))
        screen.blit(puitE,(483,350))
        screen.blit(puitF,(543,350))
        screen.blit(puit2,(700,255))
    #AI
        puitG= font.render(str(mancala_UI.puits[7].nbGraines),True,(0,0,0))
        puitH= font.render(str(mancala_UI.puits[8].nbGraines),True,(0,0,0))
        puitI= font.render(str(mancala_UI.puits[9].nbGraines),True,(0,0,0))
        puitJ= font.render(str(mancala_UI.puits[10].nbGraines),True,(0,0,0))
        puitK= font.render(str(mancala_UI.puits[11].nbGraines),True,(0,0,0))
        puitL= font.render(str(mancala_UI.puits[12].nbGraines),True,(0,0,0))
        puit1= font.render(str(mancala_UI.puits[13].nbGraines),True,(0,0,0))

        screen.blit(puitG,(207,170))
        screen.blit(puitH,(265,170))
        screen.blit(puitI,(325,170))
        screen.blit(puitJ,(423,170))
        screen.blit(puitK,(483,170))
        screen.blit(puitL,(543,170))
        screen.blit(puit1,(90,255))

    def show_puit_img():
        for i in mancala_UI.puits:
            screen.blit(i.bouton,(i.x,i.y))

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


    while True:
        # mettre le background en blanc
        screen.fill((255,255,255))

# affiche le board dans screen
        screen.blit(board,(boardX,boardY))

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
                pygame.quit()

#event click mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos # recup la position de la souris

                for index, key in enumerate(mancala.grille):
             
             # vu que la listPuitCollider est sync avec la grille et les puits quand tu 
             # click sur un collider avec son index tu prend le puit de la grille qui a le meme index et tu effectue la fonction
                    if click_dectection(listPuitCollider[index], pos):
                        print('The mouse is over the rectangle')
                        mancala.joueurDeplacement(key)
                       
                        update_puits()

        
        
        orderManager()
    
   # show_puit(puits[0].x, puits[0].y)
        pygame.display.update()


def main_menu():
    rect_width = 400
    rect_height = 70
    quit_btn = pygame.Rect(200,200,rect_width, rect_height)

   

    # dessine le rectangle
    quit_box = pygame.Surface(quit_btn.size,pygame.SRCALPHA)
    pygame.draw.rect(quit_box,(255,255,255),quit_box.get_rect())
    

    while True:
        screen.fill((0,0,0))
        screen.blit(quit_box, (quit_btn.x,quit_btn.y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos 
                if click_dectection(quit_btn,pos):
                    play()

            
        

        pygame.display.update()
main_menu()