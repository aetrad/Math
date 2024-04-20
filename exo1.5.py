import numpy as np

# Générer une matrice aléatoire
n, m = 3, 3  # Dimensions de la matrice
matrice = np.random.randint(-10, 10, (n, m))

# Demander à l'utilisateur de saisir un scalaire
scalaire = float(input("Entrez un scalaire : "))

# Calculer le produit de la matrice par le scalaire
produit = matrice * scalaire

# Afficher les résultats
print("Matrice originale :")
print(matrice)
print("\nScalaire :", scalaire)
print("\nProduit de la matrice par le scalaire :")
print(produit)
