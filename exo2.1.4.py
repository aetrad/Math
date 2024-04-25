import numpy as np

# Partie 1: Création et affichage de la matrice M
M = np.array([[4.1, 2.0, 0], [4.6, 1, 6], [2, 8, 3]], dtype=float)
print("Matrice M:")
print(M)

# Partie 2: Affichage de l'élément m23
# Attention, l'indexation commence à 0, donc m23 est à l'index [1][2]
print("Élément m23 :", M[1][2])

# Partie 3: Affichage de la 3ème ligne
print("3ème ligne de M:")
print(M[2])

# Partie 4: Affichage de la première colonne
print("Première colonne de M:")
print(M[:, 0])

# Partie 5: Création et affichage d'une matrice 3x3 de type entier ne contenant que des 1
matrice_uns = np.ones((3, 3), dtype=int)
print("Matrice de 1s:")
print(matrice_uns)

# Partie 6: Création et affichage d'une matrice unité diagonale 5x5
matrice_identite = np.eye(5, dtype=float)
print("Matrice unité 5x5:")
print(matrice_identite)

# Partie 7: Réarrangement d'une liste linéaire en une matrice 3x2
A = np.array([2, 4, 6, 12, 24, 36])
A_reshape = A.reshape(3, 2)
print("Matrice 3x2 A:")
print(A_reshape)
