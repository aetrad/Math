import numpy as np

# Demander à l'utilisateur d'entrer les dimensions de la matrice
n = int(input("Entrez le nombre de lignes de la matrice : "))
m = int(input("Entrez le nombre de colonnes de la matrice : "))

# Générer une matrice aléatoire d'entiers
matrice_entiers = np.random.randint(low=0, high=100, size=(n, m))

# Générer une matrice aléatoire de réels
matrice_reels = np.random.rand(n, m)

# Afficher les matrices
print("Matrice aléatoire d'entiers :")
print(matrice_entiers)
print("\nMatrice aléatoire de réels :")
print(matrice_reels)
