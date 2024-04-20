import numpy as np

# Définir la taille de la matrice aléatoire
n, m = 3, 4  # Exemple avec une matrice de 3 lignes et 4 colonnes

# Générer la matrice aléatoire
matrice = np.random.randint(1, 10, size=(n, m))
print("Matrice aléatoire :")
print(matrice)

# Première méthode pour calculer la somme des colonnes : Transposer puis utiliser une boucle
somme_colonnes_method1 = np.array([sum(colonne) for colonne in matrice.T])
print("\nSomme des colonnes (méthode 1) :")
print(somme_colonnes_method1)

# Deuxième méthode pour calculer la somme des colonnes : Utiliser np.sum avec axis=0
somme_colonnes_method2 = np.sum(matrice, axis=0)
print("\nSomme des colonnes (méthode 2) :")
print(somme_colonnes_method2)
