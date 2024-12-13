from navire import Navire
from plateau import Plateau

class Player:
    def __init__(self, name):
        self.name = name
        self.plateau = Plateau()
        self.navire = Navire()
        
