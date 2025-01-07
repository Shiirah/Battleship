from navire import PorteAvion, Croiseur, Destroyer, SousMarin
from plateau import Plateau
from tkinter import messagebox
import random
import tkinter as tk

class Player:
    def __init__(self, name):
        self.name = name
        self.plateau = Plateau()
        self.navires = []
        self.nbNavire = 0

    def placerNavireRandom(self):
        navires = [PorteAvion(), Croiseur(), Destroyer(), Destroyer(), SousMarin(), SousMarin()]
        while self.nbNavire < len(navires):
            navire = navires[self.nbNavire]
            orientationNavire = random.randint(0, 1)
            posX = random.randint(0, len(self.plateau.board) - 1)
            posY = random.randint(0, len(self.plateau.board[0]) - 1)

            if orientationNavire == 0:
                navire.pos = [(posX, posY + i) for i in range(navire.taille) if posY + i < len(self.plateau.board[0])]
            else:
                navire.pos = [(posX + i, posY) for i in range(navire.taille) if posX + i < len(self.plateau.board)]

            if len(navire.pos) == navire.taille and self.plateau.checkPossiblePlacer(navire):
                for (x, y) in navire.pos:
                    self.plateau.board[x][y] = 1
                self.nbNavire += 1
                self.navires.append(navire)

