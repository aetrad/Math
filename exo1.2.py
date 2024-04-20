import numpy as np

n = int(input("Entrez la taille de la matrice unité : "))
matrice_unite = np.eye(n)
print("Matrice unité :")
print(matrice_unite)

diagonale = np.random.randint(1, 10, size=n)
matrice_diagonale = np.diag(diagonale)
print("Matrice diagonale :")
print(matrice_diagonale)

matrice_triangulaire_sup = np.triu(np.random.rand(n, n))
print("Matrice triangulaire supérieure :")
print(matrice_triangulaire_sup)

matrice_creuse = np.zeros((n, n))
for _ in range(n):  # Ajouter n éléments non nuls pour simplifier
    i, j = np.random.randint(0, n, 2)
    matrice_creuse[i, j] = np.random.randint(1, 10)
print("Matrice creuse :")
print(matrice_creuse)

matrice_nulle = np.zeros((n, n))
print("Matrice nulle :")
print(matrice_nulle)
