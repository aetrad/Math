import numpy as np

# Générer une matrice aléatoire
n, m = 4, 3  # Définir les dimensions de la matrice, par exemple 4 lignes et 3 colonnes
matrice = np.random.randint(1, 10, (n, m))
print("Matrice originale :")
print(matrice)

# Calculer la transposée de la matrice
transposee = matrice.T
print("\nMatrice transposée :")
print(transposee)
