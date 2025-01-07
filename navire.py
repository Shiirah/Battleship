import random

class Navire:
    # Classe navire + heritage pour chaque type de navire 
    # Chaque navire a une liste de position, une taille et un nombre de navire en fonction du type récupérer en paramètre lors de l'heritage
    def __init__(self,taille):
        self.taille = taille
        self.pos = []
        self.hits = [False] * self.taille

    def __repr__(self):
        return str(self.pos)

#retourne true si tous les élements de hits sont True 
    def isDead(self):
        return all(self.hits)
    
class PorteAvion(Navire):
    def __init__(self):
        super().__init__(5)
        self.nbNavire = 1

class Croiseur(Navire):
    def __init__(self):
        super().__init__(4)
        self.nbNavire = 1

class Destroyer(Navire):
    def __init__(self):
        super().__init__(3)
        self.nbNavire = 2

class SousMarin(Navire):
    def __init__(self):
        super().__init__(2)
        self.nbNavire = 2




    
    

