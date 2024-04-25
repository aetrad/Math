import numpy as np

# Définir les matrices A, B et C
A = np.array([[4.1, 2.0, 0], [4.6, 1, 6], [2, 8, 3]])
B = np.array([[1, 1, 0], [1.0, 1, 1], [2, 2, 2]])
C = np.array([[1, 2], [0, 1], [3, 1]])

# Afficher les matrices A, B, et C
print("Matrice A:")
print(A)
print("Matrice B:")
print(B)
print("Matrice C:")
print(C)

# Produit d'Hadamard (élément par élément)
Hadamard_AB = A * B
print("Produit d'Hadamard A x B:")
print(Hadamard_AB)

# Produit matriciel A@B
Produit_AB = A @ B
print("Produit matriciel A @ B:")
print(Produit_AB)

# Produit matriciel sans utiliser l'opérateur @
def produit_matriciel(X, Y):
    # Vérification de la compatibilité des matrices
    if X.shape[1] != Y.shape[0]:
        return "Produit matriciel impossible, dimensions incompatibles."
    # Initialisation du résultat
    resultat = np.zeros((X.shape[0], Y.shape[1]))
    # Calcul du produit matriciel
    for i in range(X.shape[0]):
        for j in range(Y.shape[1]):
            for k in range(X.shape[1]):
                resultat[i][j] += X[i][k] * Y[k][j]
    return resultat

# Calculer A x B sans utiliser '@'
print("Produit matriciel A x B sans utiliser '@':")
print(produit_matriciel(A, B))

# Essayer de calculer A x C
print("Essayer de calculer le produit matriciel A x C:")
print(produit_matriciel(A, C))

# Essayer de calculer C x A
print("Essayer de calculer le produit matriciel C x A:")
print(produit_matriciel(C, A))
