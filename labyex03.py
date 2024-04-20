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

    # Choix aléatoire de l'entrée et de la sortie
    entree = random.choice([(x, 0) for x in range(largeur)])
    sortie = random.choice([(x, hauteur-1) for x in range(largeur)])

    pile = [entree]
    visite = set([entree])

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

            if suivant == sortie:
                break

    return labyrinthe, entree, sortie

def afficher_labyrinthe(labyrinthe, largeur, hauteur, entree, sortie):
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

    # Entrée
    plt.plot(entree[0]+0.5, entree[1]+0.5, 'ro')  # Entrée en rouge

    # Sortie
    plt.plot(sortie[0]+0.5, sortie[1]+0.5, 'bo')  # Sortie en bleu

    plt.xticks(range(largeur+1))
    plt.yticks(range(hauteur+1))
    plt.grid(True)
    plt.show()

largeur = int(input("Entrez la largeur du labyrinthe : "))
hauteur = int(input("Entrez la hauteur du labyrinthe : "))

labyrinthe, entree, sortie = generer_labyrinthe(largeur, hauteur)
afficher_labyrinthe(labyrinthe, largeur, hauteur, entree, sortie)
