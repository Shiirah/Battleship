import random
import tkinter as tk
from navire import Navire, PorteAvion, Croiseur, Destroyer, SousMarin
from plateau import Plateau
from player import Player

################# Variable #####################

ordi = Player("Ordinateur")
ordi.placerNavireRandom()

navireDeadOrdi = {
    "PorteAvion": 0,
    "Croiseur": 0, 
    "Destroyer": 0, 
    "SousMarin": 0
    }

player = Player("Player")
player.placerNavireRandom()

navireDeadPlayer = {
    "PorteAvion": 0,
    "Croiseur": 0, 
    "Destroyer": 0, 
    "SousMarin": 0
    }

plateau = Plateau()
board = plateau.board

#################### Fonction ####################
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

def checkFin():
    if all(navire.isDead() for navire in ordi.navires):
        print("gg ez")
        return True
    if all(navire.isDead() for navire in player.navires):
        print("rip")
        return True
    return False

def tirer(x, y):
    if ordi.plateau.board[x][y] == 1:
        board_adverse[x][y].config(text="X", bg="red", state="disabled")
        for navire in ordi.navires:
            if (x, y) in navire.pos:
                index = navire.pos.index((x, y))
                navire.hits[index] = True
                if navire.isDead():
                    type_navire = type(navire).__name__
                    navireDeadOrdi[type_navire] += 1
                    majDead(frameDeadOrdi, navireDeadOrdi, "Navires coulés adversaire")
    else:
        board_adverse[x][y].config(text="O", bg="blue", state="disabled")

    if checkFin():
        victoire("Joueur")
    else:
        tir_ordi()

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
                if navire.isDead():
                    type_navire = type(navire).__name__
                    navireDeadPlayer[type_navire] += 1
                    majDead(frameDeadPlayer, navireDeadPlayer, "Navires coulés joueur")
    else:
        mon_board[x][y].config(text="O", bg="blue")
        player.plateau.board[x][y] = 'O'

    if checkFin():
        victoire("Ordinateur")

def majDead(frame, data, titre):
    for widget in frame.winfo_children():
        widget.destroy()
    
    tk.Label(frame, text=titre, font=("Arial", 12, "bold")).pack()
    
    for navire, count in data.items():
        tk.Label(frame, text=f"{navire}: {count}").pack()

################### Tkinter app ###################

mainapp = tk.Tk()
mainapp.title('Battleship')


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

tk.Label(mainapp, text="Plateau adverse", font=("Arial", 14)).grid(row=len(board)+2, column=0, columnspan=10)

board_adverse = [[None for _ in range(len(board))] for _ in range(len(board))]
for i in range(len(board)):
    for j in range(len(board)):
        cellule = tk.Button(mainapp, text='', width=5, height=2, command=lambda x=i, y=j: tirer(x, y))
        cellule.grid(row=i+len(board)+3, column=j)
        board_adverse[i][j] = cellule

frameDeadOrdi = tk.Frame(mainapp, relief="ridge", borderwidth=2)
frameDeadOrdi.grid(row=15, column=22, rowspan=5, padx=10, pady=5)
majDead(frameDeadOrdi, navireDeadOrdi, "Navires coulés adversaire")

frameDeadPlayer = tk.Frame(mainapp, relief="ridge", borderwidth=2)
frameDeadPlayer.grid(row=3, column=22, rowspan=5, padx=10, pady=5)
majDead(frameDeadPlayer, navireDeadPlayer, "Navires coulés joueur")

mainapp.mainloop()
