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
     
    

    grilleA= font.render(str(mancala.grille.get("A")),True,(0,0,0))
    grilleB= font.render(str(mancala.grille.get("B")),True,(0,0,0))
    grilleC= font.render(str(mancala.grille.get("C")),True,(0,0,0))
    grilleD= font.render(str(mancala.grille.get("D")),True,(0,0,0))
    grilleE= font.render(str(mancala.grille.get("E")),True,(0,0,0))
    grilleF= font.render(str(mancala.grille.get("F")),True,(0,0,0))

    screen.blit(grilleA,(207,285))
    screen.blit(grilleB,(265,285))
    screen.blit(grilleC,(325,285))
    screen.blit(grilleD,(423,285))
    screen.blit(grilleE,(483,285))
    screen.blit(grilleF,(543,285))

def show_score(x,y):
    score = font.render("Score: "+ str(score_value),True,(0,0,0))
    screen.blit(score,(x,y))


puits = []
puits.append(Puit("A", 562, 308, 5))

#puit_info =  puit.label +"-"+str(puit.nbGraines) +"-"+str(puit.x)+"-"+str(puit.y)
#test_puit =  font.render(puit_info,True,(0,0,0))


puits.append(Puit("B", 562, 308, 5))
puits.append(Puit("C", 562, 308, 5))
puits.append(Puit("D", 562, 308, 5))
puits.append(Puit("E", 562, 308, 5))
puits.append(Puit("F", 562, 308, 5))

#def show_puit(x,y):
  # puits[0] = font.render(str(puits[0].nbGraines),True,(0,0,0))
   #screen.blit(puits[0],(x,y))

#   
def is_over(rect, pos):
    # function takes a tuple of (x, y) coords and a pygame.Rect object
    # returns True if the given rect overlaps the given coords
    # else it returns False
    return True if rect.collidepoint(pos[0], pos[1]) else False

 # rectangle colour
rect_colour = (255,0,0)

# define the x, y, width & height for the rectangle
arrayRecAndGrille = {
            0: "A",
            1 :"B",
            2: "C",
            3: "D",
            4: "E",
            5: "F",
            6: "2",
            7: "L",
            8: "K",
            9: "J",
            10: "I",
            11: "H",
            12: "G",
            13: "1",
}
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
    pygame.draw.rect(box, 0,box.get_rect())
    screen.blit(box, (x,y))



running = True
while running:
    
# mettre le background en blanc
    screen.fill((255,255,255))

# mettre le board dans screen
    screen.blit(background,(backgroundX,backgroundY))
#mettre les box collider des puits
    puit_collider(207,285)
    puit_collider(265,285)
    puit_collider(325,285)
    puit_collider(423,285)
    puit_collider(483,285)
    puit_collider(543,285)

    show_grille()
    for event in pygame.event.get():
# event fermer window
        if event.type == pygame.QUIT:
            running = False
#event click mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos # recup la position de la souris
            if is_over(rectangles[0], pos): # pass in the pygame.Rect and the mouse coords
                print('The mouse is over the rectangle')
                print(rectangles[0])
                print(arrayRecAndGrille.get(0))
                mancala.joueurDeplacement("A")
               
                print(mancala.grille)
            elif is_over(rectangles[1], pos):
                print('The mouse is over the rectangle')
                mancala.joueurDeplacement("B")
                print(mancala.grille)
            elif is_over(rectangles[2], pos):
                print('The mouse is over the rectangle')
            elif is_over(rectangles[3], pos):
                print('The mouse is over the rectangle')
            elif is_over(rectangles[4], pos):
                print('The mouse is over the rectangle')
            elif is_over(rectangles[5], pos):
                print('The mouse is over the rectangle')    
            else:
                print('The mouse is not over the rectangle')
                print(pos)
    
           
            


        
        
    show_score(textX,textY)
   # show_puit(puits[0].x, puits[0].y)
    pygame.display.update()