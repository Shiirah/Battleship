import random

class Navire:
    def __init__(self, taille, position):
        self.taille = taille
        self.pos = []
        self.hits = [False] * 2


#retourne true si tous les élements de hits sont True 
    def isDead(self):
        return all(self.hits)
    
    def choixTaille(self):
        self.taille = random.randint(1,3)


