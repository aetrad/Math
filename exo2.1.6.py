import numpy as np

def creer_matrice():
    # Demander les dimensions de la matrice
    rows = int(input("Entrez le nombre de lignes de la matrice : "))
    cols = int(input("Entrez le nombre de colonnes de la matrice : "))
    
    # Créer la matrice avec des entrées de l'utilisateur
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Entrez les éléments de la ligne {i+1} séparés par des espaces : ").split()))
        matrix.append(row)
    
    return np.array(matrix)

# Création des matrices A et B
print("Création de la matrice A:")
A = creer_matrice()
print("Création de la matrice B:")
B = creer_matrice()

# Produit matriciel A*B et B*A
try:
    produit_AB = np.dot(A, B)
    print("Produit matriciel A x B:")
    print(produit_AB)
except ValueError:
    print("Le produit matriciel A x B n'est pas possible à cause des dimensions incompatibles.")

try:
    produit_BA = np.dot(B, A)
    print("Produit matriciel B x A:")
    print(produit_BA)
except ValueError:
    print("Le produit matriciel B x A n'est pas possible à cause des dimensions incompatibles.")

# Addition de A et B
try:
    somme_AB = A + B
    print("Somme de A et B:")
    print(somme_AB)
except ValueError:
    print("La somme de A et B n'est pas possible à cause des dimensions incompatibles.")

# Transposée de A
transpose_A = A.T
print("Transposée de A:")
print(transpose_A)
print(f"Nombre de lignes : {transpose_A.shape[0]}, Nombre de colonnes : {transpose_A.shape[1]}")
