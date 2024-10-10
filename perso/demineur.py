import random
import tkinter
from tkinter import *

# Paramètres du jeu
longueur = 10
largeur = 10
bombe = 6
c = 50  # Taille des cases
partie_en_cours = True

# Initialisation de la carte (grille)
def generer_carte():
    carte = [[0 for i in range(longueur)] for i in range(largeur)]
    nb_bombes = bombe

    # Placement des bombes aléatoirement
    while nb_bombes != 0:
        i = random.randint(0, longueur - 1)
        j = random.randint(0, largeur - 1)
        if carte[i][j] != 'X':
            carte[i][j] = 'X'
            nb_bombes -= 1

    # Calcul des numéros autour des bombes
    for i in range(largeur):
        for j in range(longueur):
            if carte[i][j] != 'X':
                s = 0
                if i - 1 >= 0 and j - 1 >= 0 and carte[i - 1][j - 1] == 'X':
                    s += 1
                if i - 1 >= 0 and carte[i - 1][j] == 'X':
                    s += 1
                if j - 1 >= 0 and carte[i][j - 1] == 'X':
                    s += 1
                if i + 1 < largeur and j + 1 < longueur and carte[i + 1][j + 1] == 'X':
                    s += 1
                if i + 1 < largeur and carte[i + 1][j] == 'X':
                    s += 1
                if j + 1 < longueur and carte[i][j + 1] == 'X':
                    s += 1
                if i + 1 < largeur and j - 1 >= 0 and carte[i + 1][j - 1] == 'X':
                    s += 1
                if i - 1 >= 0 and j + 1 < longueur and carte[i - 1][j + 1] == 'X':
                    s += 1
                carte[i][j] = s
    return carte

# Fonction pour recommencer la partie
def recommencer_partie():
    global carte, revelees, partie_en_cours
    carte = generer_carte()
    dessin.delete("all")  # Efface toutes les cases précédentes
    afficher_grille()
    revelees = [[False for _ in range(longueur)] for _ in range(largeur)]  # Reset des cases révélées
    partie_en_cours = True  # Réinitialiser la partie

# Fonction pour afficher les cases non-bombées adjacentes
def reveler_voisins(x, y):
    # Si la case est déjà révélée, on ne fait rien
    if revelees[y][x]:
        return
    
    # Révèle la case actuelle
    revelees[y][x] = True
    dessin.itemconfigure(cases[y][x], fill='gray')
    
    if carte[y][x] > 0:
        # Affiche le nombre de bombes autour si > 0
        dessin.create_text(x * c + c // 2, y * c + c // 2, text=str(carte[y][x]), font=('Helvetica', 18), fill='black')
    else:
        # Si la case ne contient pas de bombes autour, on révèle les voisins
        voisins = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for vx, vy in voisins:
            nx, ny = x + vx, y + vy
            if 0 <= nx < longueur and 0 <= ny < largeur and not revelees[ny][nx] and carte[ny][nx] != 'X':
                reveler_voisins(nx, ny)

# Fonction pour vérifier si toutes les cases non-bombées sont révélées (victoire)
def verifier_victoire():
    for i in range(largeur):
        for j in range(longueur):
            if carte[i][j] != 'X' and not revelees[i][j]:
                return False
    return True

# Fonction qui gère les clics sur les cases
def clic_case(event):
    global partie_en_cours
    if not partie_en_cours:
        return  # Si la partie est finie, on ignore les clics

    x = event.x // c
    y = event.y // c
    if carte[y][x] == 'X':  # Si on clique sur une bombe
        dessin.itemconfigure(cases[y][x], fill='red')  # On révèle la bombe
        print("Perdu !")
        afficher_message_perdu()
        partie_en_cours = False  # La partie est terminée
    else:
        reveler_voisins(x, y)  # Révèle la case et les cases adjacentes
        if verifier_victoire():  # Vérifie si toutes les cases non-bombées sont révélées
            afficher_message_victoire()
            partie_en_cours = False  # La partie est terminée

# Fonction pour afficher un message de défaite
def afficher_message_perdu():
    perdu_label = Label(fen, text="Perdu !", font=('Helvetica', 18), fg='red')
    perdu_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Fonction pour afficher un message de victoire
def afficher_message_victoire():
    victoire_label = Label(fen, text="Gagné !", font=('Helvetica', 18), fg='green')
    victoire_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Création des cases et affichage de la grille
def afficher_grille():
    global cases
    cases = []
    for ligne in range(longueur):
        transit = []
        for colonne in range(largeur):
            case = dessin.create_rectangle(colonne * c + 2, ligne * c + 2, (colonne + 1) * c + 2, (ligne + 1) * c + 2)
            transit.append(case)
        cases.append(transit)

# Interface graphique
fen = Tk()
fen.title('Démineur')

# Bouton pour quitter
bouton_quitter = Button(fen, text='Quitter', command=fen.destroy)
bouton_quitter.grid(row=1, column=1, sticky=W+E, padx=3, pady=3)

# Bouton pour recommencer la partie
bouton_recommencer = Button(fen, text='Recommencer', command=recommencer_partie)
bouton_recommencer.grid(row=1, column=0, sticky=W+E, padx=3, pady=3)

# Canvas pour dessiner les cases
dessin = Canvas(fen, width=largeur * c + 2, height=longueur * c + 2, bg='white')
dessin.grid(row=0, column=0, columnspan=2, padx=3, pady=3)

# Ajout de la détection de clic sur chaque case
dessin.bind("<Button-1>", clic_case)  # Left mouse button click

# Initialisation de la carte et affichage de la grille
carte = generer_carte()
revelees = [[False for _ in range(longueur)] for _ in range(largeur)]  # Table des cases révélées
afficher_grille()

fen.mainloop()

