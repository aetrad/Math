import numpy as np

# Définir la taille de la matrice aléatoire
n, m = 3, 4  # Par exemple, une matrice de 3 lignes et 4 colonnes

# Générer la matrice aléatoire
matrice = np.random.randint(1, 10, size=(n, m))
print("Matrice aléatoire :")
print(matrice)

# Première méthode pour calculer la somme des lignes : Utiliser une boucle
somme_lignes_method1 = np.array([sum(ligne) for ligne in matrice])
print("\nSomme des lignes (méthode 1) :")
print(somme_lignes_method1)

# Deuxième méthode pour calculer la somme des lignes : Utiliser np.sum avec axis=1
somme_lignes_method2 = np.sum(matrice, axis=1)
print("\nSomme des lignes (méthode 2) :")
print(somme_lignes_method2)
