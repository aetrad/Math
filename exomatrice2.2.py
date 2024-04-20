def transvection(matrice, k, i, alpha):
    if k < 0 or i < 0 or k >= len(matrice) or i >= len(matrice):
        print("Indices de ligne invalides.")
        return

    ligne_modifiee = [matrice[k][j] - alpha * matrice[i][j] for j in range(len(matrice[k]))]
    matrice[k] = ligne_modifiee

# Exemple d'utilisation :
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print("Matrice avant transvection :")
for ligne in A:
    print(ligne)

transvection(A, 1, 0, 2)

print("\nMatrice après transvection :")
for ligne in A:
    print(ligne)
