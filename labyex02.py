import random
import matplotlib.pyplot as plt

def voisins(cell, largeur, hauteur):
    x, y = cell
    results = []
    if x > 0: results.append((x-1, y))  # Gauche
    if y > 0: results.append((x, y-1))  # Bas
    if x < largeur-1: results.append((x+1, y))  # Droite
    if y < hauteur-1: results.append((x, y+1))  # Haut
    return results

def generer_labyrinthe(largeur, hauteur):
    labyrinthe = {(x, y):['N', 'S', 'E', 'O'] for x in range(largeur) for y in range(hauteur)}
    start = (random.randint(0, largeur-1), random.randint(0, hauteur-1))
    pile = [start]
    visite = set([start])
    chemin = []

    while pile:
        cell = pile[-1]
        voisins_non_visites = [v for v in voisins(cell, largeur, hauteur) if v not in visite]

        if not voisins_non_visites:
            pile.pop()
        else:
            suivant = random.choice(voisins_non_visites)
            x, y = cell
            xs, ys = suivant
            if x < xs:  # Suivant est à droite
                labyrinthe[cell].remove('E')
                labyrinthe[suivant].remove('O')
            elif x > xs:  # Suivant est à gauche
                labyrinthe[cell].remove('O')
                labyrinthe[suivant].remove('E')
            elif y < ys:  # Suivant est en haut
                labyrinthe[cell].remove('N')
                labyrinthe[suivant].remove('S')
            elif y > ys:  # Suivant est en bas
                labyrinthe[cell].remove('S')
                labyrinthe[suivant].remove('N')

            pile.append(suivant)
            visite.add(suivant)
            chemin.append(cell)

    return labyrinthe, chemin

def afficher_labyrinthe(labyrinthe, largeur, hauteur, chemin):
    plt.figure(figsize=(largeur, hauteur))
    for y in range(hauteur):
        for x in range(largeur):
            if 'N' in labyrinthe[(x, y)]:
                plt.plot([x, x+1], [y+1, y+1], 'k-')  # Mur du haut
            if 'S' in labyrinthe[(x, y)]:
                plt.plot([x, x+1], [y, y], 'k-')      # Mur du bas
            if 'E' in labyrinthe[(x, y)]:
                plt.plot([x+1, x+1], [y, y+1], 'k-')  # Mur de droite
            if 'O' in labyrinthe[(x, y)]:
                plt.plot([x, x], [y, y+1], 'k-')      # Mur de gauche

    # Dessiner le chemin
    for i in range(len(chemin) - 1):
        x1, y1 = chemin[i]
        x2, y2 = chemin[i+1]
        plt.plot([x1+0.5, x2+0.5], [y1+0.5, y2+0.5], 'g-', linewidth=2)

    plt.xticks(range(largeur+1))
    plt.yticks(range(hauteur+1))
    plt.grid(True)
    plt.show()

largeur = int(input("Entrez la largeur du labyrinthe : "))
hauteur = int(input("Entrez la hauteur du labyrinthe : "))

labyrinthe, chemin = generer_labyrinthe(largeur, hauteur)
afficher_labyrinthe(labyrinthe, largeur, hauteur, chemin)
