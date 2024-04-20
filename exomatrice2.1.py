def inverse_lignes(matrice, i, j):
    if i < 0 or j < 0 or i >= len(matrice) or j >= len(matrice):
        print("Indices de ligne invalides.")
        return

    matrice[i], matrice[j] = matrice[j], matrice[i]

# Exemple d'utilisation :
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print("Matrice avant l'inversion :")
for ligne in A:
    print(ligne)

inverse_lignes(A, 0, 2)

print("\nMatrice après l'inversion :")
for ligne in A:
    print(ligne)
