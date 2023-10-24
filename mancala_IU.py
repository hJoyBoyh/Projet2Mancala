
from Puit import Puit


class Mancala_UI:
    def __init__(self):
        self.puits = []
        self.puits.append(Puit("A", 198,280, 4,("images/4.jpg")))
        self.puits.append(Puit("B", 259,280, 4 ,("images/4.jpg")))
        self.puits.append(Puit("C", 319,280, 4 ,("images/4.jpg")))
        self.puits.append(Puit("D", 417, 280, 4 ,("images/4.jpg")))
        self.puits.append(Puit("E", 478, 280, 4 ,("images/4.jpg")))
        self.puits.append(Puit("F", 536, 280, 4 ,("images/4.jpg")))
        self.puits.append(Puit("2", 595, 210, 0 ,("images/se.jpg")))
        self.puits.append(Puit("L", 198, 210, 4 ,("images/4.jpg")))
        self.puits.append(Puit("K", 259, 210, 4 ,("images/4.jpg")))
        self.puits.append(Puit("J", 319, 210, 4 ,("images/4.jpg")))
        self.puits.append(Puit("I", 417, 210, 4 ,("images/4.jpg")))
        self.puits.append(Puit("H", 478, 210, 4 ,("images/4.jpg")))
        self.puits.append(Puit("G", 536, 210, 4 ,("images/4.jpg")))
        self.puits.append(Puit("1", 140, 210, 0 ,("images/se.jpg")))

