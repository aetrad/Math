import numpy as np

# Remplacez 3, 3 par les dimensions souhaitées
n, m = 3, 3

# Créer une matrice aléatoire
matrice = np.random.randint(-10, 10, (n, m))

# Calculer l'opposée de la matrice
matrice_opposee = -matrice

# Afficher les deux matrices
print("Matrice originale:")
print(matrice)
print("\nMatrice opposée:")
print(matrice_opposee)

# Vérifier que leur somme fait bien une matrice nulle
somme = matrice + matrice_opposee
print("\nSomme des deux matrices:")
print(somme)

# Vérification
verification = np.all(somme == 0)
print("\nLa somme des deux matrices est bien une matrice nulle:", verification)
