from navire import Navire
import random

class Plateau:
    # créer la grille sur laquel se base le grid tkinter
    def __init__(self):
        self.board = [[0 for i in range(10)] for j in range(10)]
    # parcours la liste des pos du navire qui appelle la methode et check si elle depasse du plateau ou non, retour true si non
    # prend en paramètre un navire à checker
    def checkPossiblePlacer(self, navire):
        for (x,y) in navire.pos:
            if x < 0 or y < 0 or x >= len(self.board) or y >= len(self.board):
                return False
            if self.board[x][y] != 0:
                return False
        return True
    

