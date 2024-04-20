import numpy as np

# Générer une matrice carrée aléatoire
n = 3  # Taille de la matrice carrée
matrice = np.random.randint(1, 10, size=(n, n))
print("Matrice carrée aléatoire :")
print(matrice)

# Demander à l'utilisateur la puissance désirée
puissance = int(input("Entrez la puissance désirée (n) : "))

# Calculer la n-ième puissance de la matrice
matrice_puissance = np.linalg.matrix_power(matrice, puissance)

# Afficher le résultat
print(f"La matrice élevée à la puissance {puissance} :")
print(matrice_puissance)
