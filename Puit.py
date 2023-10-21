import pygame
class Puit:
    def __init__(self, label, x, y, nbGraines,bouton):
        self.label = label
        self.x = x
        self.y = y
        self.nbGraines = nbGraines
        self.bouton = pygame.image.load(bouton)
        