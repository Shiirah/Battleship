from navire import Navire
import random

class Plateau:
    def __init__(self):
        # self.navire = Navire()
        self.board = [[0 for i in range(10)] for j in range(10)]
        print(self.board)

        for i in self.board:
            print(i)

    def checkPossible(self):
        for (x,y) in self.navire.pos:
            if x < 0 or y < 0 or x > len(self.board) or y > len(self.board):
                return False
            if self.board[x][y] != 0:
                return False
        return True
    