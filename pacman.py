import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
taille_fenetre = (800, 800)
fenetre = pygame.display.set_mode(taille_fenetre)
pygame.display.set_caption("Pac-Man Labyrinthe")

# Couleurs
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)
BLEU = (0, 0, 255)

# Dimensions du labyrinthe
largeur = 10
hauteur = 10

# Fonctions pour la génération du labyrinthe
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
    entree = (0, 0)
    sortie = (largeur-1, hauteur-1)

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

    return labyrinthe, entree, sortie

# Génération du labyrinthe
labyrinthe, entree, sortie = generer_labyrinthe(largeur, hauteur)

# Taille d'une cellule
taille_cellule = 40

# Position initiale du joueur
pos_joueur = entree

# Position initiale de l'ennemi
pos_ennemi = sortie

# Vitesse de déplacement du joueur et de l'ennemi
vitesse_joueur = 1
vitesse_ennemi = 0.2

clock = pygame.time.Clock()

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Contrôles du joueur
    keys = pygame.key.get_pressed()
    deplacement_joueur = [0, 0]
    if keys[pygame.K_LEFT]:
        deplacement_joueur[0] = -vitesse_joueur
    if keys[pygame.K_RIGHT]:
        deplacement_joueur[0] = vitesse_joueur
    if keys[pygame.K_UP]:
        deplacement_joueur[1] = -vitesse_joueur
    if keys[pygame.K_DOWN]:
        deplacement_joueur[1] = vitesse_joueur

    # Déplacement du joueur
    nouvelle_pos_joueur = (pos_joueur[0] + deplacement_joueur[0], pos_joueur[1] + deplacement_joueur[1])
    if nouvelle_pos_joueur not in labyrinthe or 'S' not in labyrinthe[pos_joueur]:
        pos_joueur = nouvelle_pos_joueur

    # Déplacement de l'ennemi
    mouvements_possibles = [v for v in voisins(pos_ennemi, largeur, hauteur) if v not in labyrinthe[pos_ennemi]]
    if mouvements_possibles:
        pos_ennemi = random.choice(mouvements_possibles)

    # Effacer l'écran
    fenetre.fill(BLANC)

    # Dessiner le labyrinthe
    for cell, murs in labyrinthe.items():
        x, y = cell
        for mur in murs:
            if mur == 'N':
                pygame.draw.line(fenetre, NOIR, (x * taille_cellule, y * taille_cellule), ((x + 1) * taille_cellule, y * taille_cellule))
            elif mur == 'S':
                pygame.draw.line(fenetre, NOIR, (x * taille_cellule, (y + 1) * taille_cellule), ((x + 1) * taille_cellule, (y + 1) * taille_cellule))
            elif mur == 'E':
                pygame.draw.line(fenetre, NOIR, ((x + 1) * taille_cellule, y * taille_cellule), ((x + 1) * taille_cellule, (y + 1) * taille_cellule))
            elif mur == 'O':
                pygame.draw.line(fenetre, NOIR, (x * taille_cellule, y * taille_cellule), (x * taille_cellule, (y + 1) * taille_cellule))

    # Dessiner le joueur
    pygame.draw.rect(fenetre, BLEU, (pos_joueur[0] * taille_cellule, pos_joueur[1] * taille_cellule, taille_cellule, taille_cellule))

    # Dessiner l'ennemi
    pygame.draw.rect(fenetre, ROUGE, (pos_ennemi[0] * taille_cellule, pos_ennemi[1] * taille_cellule, taille_cellule, taille_cellule))

    # Actualiser l'écran
    pygame.display.flip()

    # Limiter la vitesse de la boucle
    clock.tick(10)
