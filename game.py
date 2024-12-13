import random
import tkinter as tk
from navire import Navire
from plateau import Plateau
from player import Player


plateau = Plateau()
board = plateau.board

mainapp = tk.Tk()
mainapp.title('Battleship')
# mainapp.geometry('500x500')


for i in range(len(board)):
    for j in range(len(board)):
        cellule = tk.Button(mainapp, text='', width=5,height=2)
        # commande a ajouter quand la fonction tirer sera up
        # cellule = tk.Button(mainapp, text='', width=5,height=2, command=fonction)
        cellule.grid(row=i,column=j)


mainapp.mainloop()