import numpy as np

def creer_matrice(n, m, nom_matrice):
    matrice = np.zeros((n, m))
    print(f"Entrez les éléments de {nom_matrice}:")
    for i in range(n):
        for j in range(m):
            matrice[i, j] = float(input(f"Elément [{i+1}, {j+1}]: "))
    return matrice

# Dimensions de la première matrice
n1 = int(input("Entrez le nombre de lignes de la première matrice: "))
m1 = int(input("Entrez le nombre de colonnes de la première matrice: "))

# Dimensions de la seconde matrice
n2 = int(input("Entrez le nombre de lignes de la seconde matrice: "))
m2 = int(input("Entrez le nombre de colonnes de la seconde matrice: "))

# Vérifier la compatibilité
if m1 != n2:
    print("Les matrices ne sont pas compatibles pour le produit.")
else:
    # Création et saisie des matrices
    matrice_A = creer_matrice(n1, m1, "Matrice A")
    matrice_B = creer_matrice(n2, m2, "Matrice B")
    
    # Calcul du produit
    produit = np.dot(matrice_A, matrice_B)
    
    # Affichage des résultats
    print("Matrice A :")
    print(matrice_A)
    print("Matrice B :")
    print(matrice_B)
    print("Produit des matrices A et B :")
    print(produit)
