import numpy as np

# Création et affichage de la matrice M
M = np.array([[4.1, 2.0, 0], [4.6, 1, 6], [2, 8, 3]])
print("Matrice M:")
print(M)

# Affichage de l'élément m23
print("\nÉlément m23 :", M[1][2])

# Affichage de la 3ème ligne
print("\n3ème ligne :", M[2])

# Affichage de la première colonne
print("\nPremière colonne :")
for ligne in M:
    print(ligne[0])

# Création et affichage d'une matrice 3x3 de type entier ne contenant que des 1
matrice_ones = np.ones((3, 3), dtype=int)
print("\nMatrice de 1:")
print(matrice_ones)

# Création et affichage d'une matrice unité diagonale 5x5 de type float
matrice_identite = np.eye(5, dtype=float)
print("\nMatrice unité diagonale 5x5:")
print(matrice_identite)

# Réarrangement et affichage de la liste linéaire A en ‘matrice’ 3x2
A = np.array([2, 4, 6, 12, 24, 36])
matrice_A = A.reshape(3, 2)
print("\nRéarrangement de la liste A en matrice 3x2:")
print(matrice_A)
