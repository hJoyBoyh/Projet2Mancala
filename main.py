import pygame
from Mancala import Mancala
from mancala_IU import Mancala_UI
from button import Button

# init the pygame
pygame.init()


#size de la fenetre

screen = pygame.display.set_mode((800,600))
#global variable
gameOver = False
rep = ""
difficulty = ""
winner =""

#instance mancala 
mancala = Mancala()
#instancier puits
mancala_UI =  Mancala_UI()
# caption set
pygame.display.set_caption("Mancala")
#background main menu
BG = pygame.image.load("assets/Background.png")

def reset_game():
    global mancala
    global mancala_UI
    mancala = Mancala()
    mancala_UI =  Mancala_UI()
    print(mancala.grille)

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)



# detection click bouton
def click_dectection(rect, pos):
    return True if rect.collidepoint(pos[0], pos[1]) else False

def play():

    global difficulty
   
    print(mancala.grille)
    
    #mancala board
    board = pygame.image.load('images/board.jpg')
    boardX = 120
    boardY = 200
    #-------------------

    # afficher tour de quel participant
    
    font = pygame.font.Font('assets/font.ttf',32)
    tourX = 10
    tourY = 10
    
    
    def show_tour(tour_value):
        score = font.render(tour_value,True,(0,0,0))
        screen.blit(score,(tourX,tourY))
        

       

#-------------------


    def event_AI():
       
        mancala.ordiDeplacement(difficulty)
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
        
         global rep
         global winner
         if gameOverCheck() or gameOver:
            evaluation = mancala.evaluate(mancala.grille)
        #print(evaluation)
            if evaluation > 0:
            
             show_tour("Winner player")
             rep = "Y"
             winner = "Winner player"
   
            elif evaluation == 0:
                show_tour("Egal")
                print("Winner egal")
                rep = "Y"
                winner = "Egal"
                
                
                
            elif evaluation < 0:
                print(f"{difficulty}AI a gagne")

                show_tour("Winner AI")
                rep = "Y"
                winner = "Winner AI"
              
                
         elif mancala.joueurTour:
            print("Tour du joueur")
            show_tour("Tour du Joueur")
         else:
            print(f"{difficulty}Tour du AI")
            show_tour("Tour du AI")
            event_AI()
         


    def updateGrill():
        
        for key, value in mancala.grille.items():
            
            for val in mancala_UI.puits:
                if key == val.label:
                    val.nbGraines = value

        orderManager()

    def event_puit(id):
        
        if mancala.joueurDeplacement(id) != False:
            updateGrill()
            
            
        else:
            
            orderManager()
            
    
    def event_reset():
        global gameOver
        global mancala
        mancala = Mancala()
        updateGrill()
        gameOver = False

    

    # change son nbGraines et son image correspondant
    def update_puits():
        
        for index, key in enumerate(mancala.grille):
            mancala_UI.puits[index].nbGraines = mancala.grille.get(mancala_UI.puits[index].label)
            print(mancala_UI.puits[index].label)
           

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
        puit1= font.render(str(mancala_UI.puits[13].nbGraines),True,(0,0,0))

        screen.blit(puitA,(207,350))
        screen.blit(puitB,(265,350))
        screen.blit(puitC,(325,350))
        screen.blit(puitD,(423,350))
        screen.blit(puitE,(483,350))
        screen.blit(puitF,(543,350))
        screen.blit(puit1,(50,255))
    #AI
        puitG= font.render(str(mancala_UI.puits[12].nbGraines),True,(0,0,0))
        puitH= font.render(str(mancala_UI.puits[11].nbGraines),True,(0,0,0))
        puitI= font.render(str(mancala_UI.puits[10].nbGraines),True,(0,0,0))
        puitJ= font.render(str(mancala_UI.puits[9].nbGraines),True,(0,0,0))
        puitK= font.render(str(mancala_UI.puits[8].nbGraines),True,(0,0,0))
        puitL= font.render(str(mancala_UI.puits[7].nbGraines),True,(0,0,0))
        puit2= font.render(str(mancala_UI.puits[6].nbGraines),True,(0,0,0))

        screen.blit(puitG,(207,170))
        screen.blit(puitH,(265,170))
        screen.blit(puitI,(325,170))
        screen.blit(puitJ,(423,170))
        screen.blit(puitK,(483,170))
        screen.blit(puitL,(543,170))
        screen.blit(puit2,(710,255))

    def show_puit_img():
        global mancala_UI
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
        puit_collider(145,255)
        puit_collider(543,220)
        puit_collider(483,220)
        puit_collider(423,220)
        puit_collider(325,220)
        puit_collider(265,220)
        puit_collider(207,220)
        
        
        
        
       
        


        updateGrill()
        update_puits()
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
                       # mancala.joueurDeplacement(key)
                        event_puit(key)
                        
                
                       
        if rep == "Y":
           
         replay()
        
           
        
        #update_puits()
        orderManager()
    
   # show_puit(puits[0].x, puits[0].y)
        pygame.display.update()
def choose_difficulty():
    bg2 = pygame.image.load("assets/Background2.png")
    while True:
        screen.fill("black")
        screen.blit(bg2, (0, 0))

        MOUSE_POS = pygame.mouse.get_pos()

        REGLE_TITLE = get_font(70).render("REGLE", True, "#b68f40")
        REGLE_RECT = REGLE_TITLE.get_rect(center=(400, 100))

        regle_instruction_1 = " Le Mancala se compose de 12 cases, d’un coffre à trésors de chaque côté et de 24 jetons au total."
        regle_instruction_2 = "Le jeu se joue à deux personnes: le premier joueur possède le côté jaune, le deuxième joueur le bleu."
        regle_instruction_3 = "Avant le début de la partie, répartir les 48 jetons de manière égale entre les 12 cases,"
        regle_instruction_6 = " il y en aura donc six dans chaque case."
        regle_instruction_4 = "Les coffres à trésors restent vides pour le moment."
        regle_instruction_5 = "SELECT YOUR DIFFICULTY"

        REGLE_TEXT_1 = get_font(7).render(regle_instruction_1, True, "#b68f40")
        REGLE_TEXT_RECT_1 = REGLE_TEXT_1.get_rect(center=(400, 200))
        REGLE_TEXT_2 = get_font(7).render(regle_instruction_2, True, "#b68f40")
        REGLE_TEXT_RECT_2 = REGLE_TEXT_2.get_rect(center=(400,215 ))
        REGLE_TEXT_3 = get_font(7).render(regle_instruction_3, True, "#b68f40")
        REGLE_TEXT_RECT_3 = REGLE_TEXT_3.get_rect(center=(400, 230))
        REGLE_TEXT_6 = get_font(7).render(regle_instruction_6, True, "#b68f40")
        REGLE_TEXT_RECT_6 = REGLE_TEXT_6.get_rect(center=(400, 240))
        REGLE_TEXT_4 = get_font(7).render(regle_instruction_4, True, "#b68f40")
        REGLE_TEXT_RECT_4 = REGLE_TEXT_4.get_rect(center=(400, 250))
        REGLE_TEXT_5 = get_font(30).render(regle_instruction_5, True, "#b68f40")
        REGLE_TEXT_RECT_5 = REGLE_TEXT_5.get_rect(center=(380, 280))
        

        
        
        screen.blit(REGLE_TITLE,REGLE_RECT)
        screen.blit(REGLE_TEXT_1,REGLE_TEXT_RECT_1)
        
        screen.blit(REGLE_TEXT_2,REGLE_TEXT_RECT_2)
        
        screen.blit(REGLE_TEXT_3,REGLE_TEXT_RECT_3)
        
        screen.blit(REGLE_TEXT_4,REGLE_TEXT_RECT_4)
        screen.blit(REGLE_TEXT_5,REGLE_TEXT_RECT_5)
        screen.blit(REGLE_TEXT_6,REGLE_TEXT_RECT_6)


        # choose difficulty

        RANDOM_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 370), 
                            text_input="RANDOM", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        MINMAX_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(200, 500), 
                            text_input="MINMAX", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        MAX_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(600, 500), 
                            text_input="MAX", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        
        for button in [MINMAX_BUTTON, MAX_BUTTON,RANDOM_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                global difficulty
                if MINMAX_BUTTON.checkForInput(MOUSE_POS):
                    difficulty = "minmax"
                    play()
                if MAX_BUTTON.checkForInput(MOUSE_POS): 
                    difficulty = "max"      
                    play()
                if RANDOM_BUTTON.checkForInput(MOUSE_POS):
                    difficulty = "random"
                    play()

        pygame.display.update()
def replay():
    pygame.time.delay(3000)
    global rep
    global winner
    rep = "n"
    while True:
        screen.blit(BG, (0, 0))

        MOUSE_POS = pygame.mouse.get_pos()

        REPLAY_TEXT = get_font(20).render(winner, True, "#b68f40")
        REPLAY_RECT = REPLAY_TEXT.get_rect(center=(400, 100))

        REPLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 250), 
                            text_input="REPLAY", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400, 400), 
                            text_input="QUIT", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

        screen.blit(REPLAY_TEXT, REPLAY_RECT)

        for button in [REPLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if REPLAY_BUTTON.checkForInput(MOUSE_POS):
                  global mancala
                  print(mancala.grille)
                  reset_game()
                  main_menu()
                   
                if QUIT_BUTTON.checkForInput(MOUSE_POS):
                    pygame.quit()
        pygame.display.update()

def main_menu():

    while True:
       
        screen.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(70).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 250), 
                            text_input="PLAY", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400, 400), 
                            text_input="QUIT", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                   # play()
                   choose_difficulty()
                
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    
        pygame.display.update()
main_menu()