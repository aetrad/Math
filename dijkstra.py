# Cours de Mathématiques pour BAC Info chapitre 2
# Opérations sur les graphes
# G. Barmarin, 2021-2022

# Exemple 3.2 : Algorithme de Dijkstra pour affichage d'un chemin

import numpy as np  # Importation de la bibliothèque mathématique

# Définition des fonctions

def dijkstraDistChemin(P, depart, arrivee):
    # Cette fonction calcule la distance minimale et le chemin le plus court
    # entre un point de départ et un point d'arrivée en utilisant l'algorithme de Dijkstra.
    pass

def dijkstra(P, depart):
    # Cette fonction implémente l'algorithme de Dijkstra pour trouver
    # le chemin le plus court à partir d'un nœud de départ.
    pass

# Programme principal

print("\nLe programme calcule un chemin le plus court et sa longueur")
print("d'un noeud vers un autre noeud du graphe s'il existe")

# Exemple de liste de villes
Z = np.array(["Paris", "Lyon", "Marseille", "Toulouse", "Nice", "Nantes", "Strasbourg", "Montpellier"])

M = np.size(Z,0)  # Nombre total de villes

print("Voici la liste des villes (", M, " villes en tout)\n")

# Affichage formaté des villes
for i in range(0, M, 4):
    print(f"{i}: {Z[i]}, {i+1}: {Z[i+1]}, {i+2}: {Z[i+2]}, {i+3}: {Z[i+3]}")

Inf = np.inf  # Définition de l'infini pour les distances non définies

# Matrice des distances entre les villes
P = np.array([
    [0, 1, Inf, Inf],
    [1, 0, 2, Inf],
    [Inf, 2, 0, 1],
    [Inf, Inf, 1, 0]
])

# Exemple d'utilisation de l'algorithme
depart = 0  # Index de la ville de départ dans la liste Z
arrivee = 2  # Index de la ville d'arrivée

# Appel de la fonction dijkstra pour calculer la distance et le chemin
dijkstraDistChemin(P, depart, arrivee)
