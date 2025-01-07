import random
import tkinter as tk
import pygame
import time
from navire import Navire, PorteAvion, Croiseur, Destroyer, SousMarin
from plateau import Plateau
from player import Player


################# Variable #####################

# instence de player/plateau + distionaire pour le compteur de navire down
ordi = Player("Ordinateur")

navireDeadOrdi = {
    "PorteAvion": 0,
    "Croiseur": 0, 
    "Destroyer": 0, 
    "SousMarin": 0
    }

player = Player("Player")

navireDeadPlayer = {
    "PorteAvion": 0,
    "Croiseur": 0, 
    "Destroyer": 0, 
    "SousMarin": 0
    }

plateau = Plateau()
board = plateau.board

# pour ajouter du son
pygame.mixer.init()
explosionSound = pygame.mixer.Sound("./assets/explosion.mp3")
gameover = pygame.mixer.Sound("./assets/gameover.mp3")
win = pygame.mixer.Sound("./assets/win.mp3")

#################### Fonction ####################

# fonction appeler lors de la victoire d'un camp, fait apparaitre un popup au centre de la page avec un message de victoire et un bouton quitter
# nomgagant a mettre en parametre quand la fonction est appelée
def victoire(nomGagnant):
    ScreenVictoire = tk.Toplevel()
    ScreenVictoire.overrideredirect(True)
    mainappWidth = mainapp.winfo_width()
    mainappHeight = mainapp.winfo_height()
    victoireWidth = 300
    victoireHeight = 200
    positionTop = (mainappHeight // 2) - (victoireWidth // 2)
    positionLeft = (mainappWidth // 2) - (victoireHeight // 2)
    ScreenVictoire.geometry(f"{victoireWidth}x{victoireHeight}+{positionLeft}+{positionTop}")
    tk.Label(ScreenVictoire, text=f"{nomGagnant} a gagné !", font=("Arial", 18, "bold")).pack(pady=20)
    
    def quitter():
        ScreenVictoire.destroy()
        mainapp.quit()
    tk.Button(ScreenVictoire, text="Quitter", command=quitter, font=("Arial", 12)).pack(pady=10)

# vérifie que tous les navires sont down et retourne true si cest le cas
def checkFin():
    if all(navire.isDead() for navire in ordi.navires):
        print("gg ez")
        return True
    if all(navire.isDead() for navire in player.navires):
        print("rip")
        return True
    return False

# fonction intégré dans les boutons pour que lors du clic, on verifie a la pos cliqué si la valeur est égale a 1
# change la couleur de la case et la désactive apres un clic et joue un son d'explosion en cas de succes
# appel le tour de l'ordi apres le tir si checkfin retourne false
def tirer(x, y):
    if ordi.plateau.board[x][y] == 1:
        board_adverse[x][y].config(text="X", bg="red", state="disabled")
        for navire in ordi.navires:
            if (x, y) in navire.pos:
                index = navire.pos.index((x, y))
                navire.hits[index] = True
                explosionSound.play()
                if navire.isDead():
                    type_navire = type(navire).__name__
                    navireDeadOrdi[type_navire] += 1
                    majDead(frameDeadOrdi, navireDeadOrdi, "Navires coulés adversaire")
    else:
        board_adverse[x][y].config(text="O", bg="blue", state="disabled")

    if checkFin():
        victoire("Joueur")
        win.play()
    else:
        tir_ordi()
# pareil
def tir_ordi():
    while True:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if player.plateau.board[x][y] not in ('X', 'O'):
            break
    if player.plateau.board[x][y] == 1:
        mon_board[x][y].config(text="X", bg="red")
        player.plateau.board[x][y] = 'X'
        for navire in player.navires:
            if (x, y) in navire.pos:
                index = navire.pos.index((x, y))
                navire.hits[index] = True
                explosionSound.play()
                if navire.isDead():
                    type_navire = type(navire).__name__
                    navireDeadPlayer[type_navire] += 1
                    majDead(frameDeadPlayer, navireDeadPlayer, "Navires coulés joueur")
    else:
        mon_board[x][y].config(text="O", bg="blue")
        player.plateau.board[x][y] = 'O'

    if checkFin():
        victoire("Ordinateur")
        gameover.play()

# chatgpt qui a fait à 100%
def majDead(frame, data, titre):
    for widget in frame.winfo_children():
        widget.destroy()
    
    tk.Label(frame, text=titre, font=("Arial", 12, "bold")).pack()
    
    for navire, count in data.items():
        tk.Label(frame, text=f"{navire}: {count}").pack()

################### Tkinter app ###################

# creation de la mainapp + titre
mainapp = tk.Tk()
mainapp.title('Battleship')

# appel de la fonction pour placer les navires de chaque joueur
# J'ai pas réussi le placement manuel
ordi.placerNavireRandom()
player.placerNavireRandom()

# titre partie haut + boucle avec la taille du tableau de plateau, chaque cellule généré aura un bouton attribué qui sera désactivé
# les cellules grisent prennent la pos des navires du player
tk.Label(mainapp, text="Mon plateau", font=("Arial", 14)).grid(row=0, column=0, columnspan=10)
mon_board = [[None for _ in range(len(board))] for _ in range(len(board))]
for i in range(len(board)):
    for j in range(len(board)):
        cellule = tk.Button(mainapp, text='', width=5, height=2, state="disabled") 
        cellule.grid(row=i+1, column=j)
        mon_board[i][j] = cellule
for navire in player.navires:
    for (x, y) in navire.pos:
        mon_board[x][y].config(bg="grey")

# titre partie bas // chaque cellule a un bouton cliquable qui passe en paramètre les coordonnés du clic a la fonction tirer
tk.Label(mainapp, text="Plateau adverse", font=("Arial", 14)).grid(row=len(board)+2, column=0, columnspan=10)
board_adverse = [[None for _ in range(len(board))] for _ in range(len(board))]
for i in range(len(board)):
    for j in range(len(board)):
        cellule = tk.Button(mainapp, text='', width=5, height=2, command=lambda x=i, y=j: tirer(x, y))
        cellule.grid(row=i+len(board)+3, column=j)
        board_adverse[i][j] = cellule


# affiche des navires down 
frameDeadOrdi = tk.Frame(mainapp, relief="ridge", borderwidth=2)
frameDeadOrdi.grid(row=15, column=22, rowspan=5, padx=10, pady=5)
majDead(frameDeadOrdi, navireDeadOrdi, "Navires coulés adversaire")

frameDeadPlayer = tk.Frame(mainapp, relief="ridge", borderwidth=2)
frameDeadPlayer.grid(row=3, column=22, rowspan=5, padx=10, pady=5)
majDead(frameDeadPlayer, navireDeadPlayer, "Navires coulés joueur")



mainapp.mainloop()
