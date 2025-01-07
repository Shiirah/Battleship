from navire import PorteAvion, Croiseur, Destroyer, SousMarin
from plateau import Plateau
from tkinter import messagebox
import random
import tkinter as tk

class Player:
    # Classe joueur
    def __init__(self, name):
        self.name = name
        self.plateau = Plateau()
        self.navires = []
        self.nbNavire = 0

    def placerNavireRandom(self):
        # Créer une liste avec les différents types de navires, puis les parcours pour leur attributer une position aléatoire
        navires = [PorteAvion(), Croiseur(), Destroyer(), Destroyer(), SousMarin(), SousMarin()]
        while self.nbNavire < len(navires):
            navire = navires[self.nbNavire]
            orientationNavire = random.randint(0, 1)
            posX = random.randint(0, len(self.plateau.board) - 1)
            posY = random.randint(0, len(self.plateau.board[0]) - 1)
            # Orientation définit en bouclant sur le x/y
            if orientationNavire == 0:
                navire.pos = [(posX, posY + i) for i in range(navire.taille) if posY + i < len(self.plateau.board[0])]
            else:
                navire.pos = [(posX + i, posY) for i in range(navire.taille) if posX + i < len(self.plateau.board)]
            # Ajout du navire si la methode checkPossiblePlacer dans plateau retour true
            if len(navire.pos) == navire.taille and self.plateau.checkPossiblePlacer(navire):
                for (x, y) in navire.pos:
                    self.plateau.board[x][y] = 1
                self.nbNavire += 1
                self.navires.append(navire)

