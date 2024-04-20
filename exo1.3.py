import numpy as np

def creer_matrice(n, m, nom_matrice):
    matrice = np.zeros((n, m))
    print(f"Entrez les éléments de {nom_matrice}:")
    for i in range(n):
        for j in range(m):
            matrice[i, j] = float(input(f"Elément [{i+1}, {j+1}]: "))
    return matrice

# Étape 1: Demander les dimensions des matrices
n = int(input("Entrez le nombre de lignes des matrices: "))
m = int(input("Entrez le nombre de colonnes des matrices: "))

# Étape 3: Création des matrices par l'utilisateur
matrice_A = creer_matrice(n, m, "Matrice A")
matrice_B = creer_matrice(n, m, "Matrice B")

# Étape 4: Addition et soustraction des matrices
addition = matrice_A + matrice_B
soustraction = matrice_A - matrice_B

# Étape 5: Afficher les résultats
print("Addition des matrices:")
print(addition)
print("Soustraction des matrices:")
print(soustraction)
