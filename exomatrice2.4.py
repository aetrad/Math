def inverse_lignes(matrice, i, j):
    if i < 0 or j < 0 or i >= len(matrice) or j >= len(matrice):
        print("Indices de ligne invalides.")
        return

    matrice[i], matrice[j] = matrice[j], matrice[i]

def transvection(matrice, k, i, alpha):
    if k < 0 or i < 0 or k >= len(matrice) or i >= len(matrice):
        print("Indices de ligne invalides.")
        return

    ligne_modifiee = [matrice[k][j] - alpha * matrice[i][j] for j in range(len(matrice[k]))]
    matrice[k] = ligne_modifiee

def gauss_jordan(matrice):
    n = len(matrice)
    m = len(matrice[0])
    r = -1  # Indice de la dernière ligne pivot

    for j in range(m):
        max_val = 0
        max_index = -1

        # Recherche du maximum dans la colonne
        for i in range(r + 1, n):
            if abs(matrice[i][j]) > max_val:
                max_val = abs(matrice[i][j])
                max_index = i

        if max_index == -1:  # Tous les éléments de la colonne sont nuls
            continue

        r += 1
        pivot = matrice[max_index][j]

        # Normalisation de la ligne pivot
        for k in range(m):
            matrice[max_index][k] /= pivot

        # Échange de la ligne pivot avec la ligne r
        if max_index != r:
            inverse_lignes(matrice, max_index, r)

        # Élimination dans les autres lignes
        for i in range(n):
            if i != r:
                coeff = matrice[i][j]
                transvection(matrice, i, r, coeff)

    return matrice

def main():
    n = int(input("Entrez le nombre de lignes de la matrice : "))
    m = int(input("Entrez le nombre de colonnes de la matrice : "))

    print("Entrez les éléments de la matrice :")
    matrice = []
    for _ in range(n):
        ligne = [float(input()) for _ in range(m)]
        matrice.append(ligne)

    matrice_inverse = gauss_jordan(matrice)

    print("\nMatrice inverse :")
    for ligne in matrice_inverse:
        print(ligne)

if __name__ == "__main__":
    main()
