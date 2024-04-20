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

def creer_matrice():
    lignes = int(input("Entrez le nombre de lignes de la matrice : "))
    colonnes = int(input("Entrez le nombre de colonnes de la matrice : "))
    matrice = []
    for _ in range(lignes):
        ligne = []
        print("Entrez les éléments de la ligne, séparés par des espaces : ")
        elements = input().split()
        if len(elements) != colonnes:
            print("Nombre incorrect d'éléments dans la ligne. Réessayez.")
            return creer_matrice()
        for element in elements:
            ligne.append(float(element))
        matrice.append(ligne)
    return matrice

def gauss_jordan(matrice):
    n = len(matrice)
    for i in range(n):
        if matrice[i][i] == 0:
            print("Le pivot est nul. Le déterminant est 0.")
            return 0

        for j in range(i+1, n):
            coeff = matrice[j][i] / matrice[i][i]
            transvection(matrice, j, i, coeff)

    determinant = 1
    for i in range(n):
        determinant *= matrice[i][i]

    return determinant

def main():
    A = creer_matrice()

    print("\nMatrice créée :")
    for ligne in A:
        print(ligne)

    determinant = gauss_jordan(A)

    print("\nDéterminant de la matrice :", determinant)

if __name__ == "__main__":
    main()
