import numpy as np

def saisir_matrice(n, m, nom_matrice):
    matrice = np.zeros((n, m))
    print(f"Entrez les éléments de la {nom_matrice}:")
    for i in range(n):
        for j in range(m):
            matrice[i, j] = float(input(f"Élément [{i+1},{j+1}]: "))
    return matrice

# Demander les dimensions des matrices
n = int(input("Nombre de lignes des matrices : "))
m = int(input("Nombre de colonnes des matrices : "))

# Saisie des matrices
matrice_A = saisir_matrice(n, m, "Matrice A")
matrice_B = saisir_matrice(n, m, "Matrice B")

# Calcul du produit de Hadamard
produit_hadamard = np.multiply(matrice_A, matrice_B)

# Affichage des résultats
print("\nMatrice A :")
print(matrice_A)
print("\nMatrice B :")
print(matrice_B)
print("\nProduit de Hadamard des matrices A et B :")
print(produit_hadamard)
