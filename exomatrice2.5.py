def creer_matrice(n, m):
    matrice = []
    for _ in range(n):
        ligne = []
        print("Entrez les coefficients de l'équation, séparés par des espaces :")
        coefficients = input().split()
        if len(coefficients) != m:
            print("Nombre incorrect de coefficients dans l'équation. Réessayez.")
            return creer_matrice(n, m)
        for coeff in coefficients:
            ligne.append(float(coeff))
        matrice.append(ligne)
    return matrice

def inverse_lignes(matrice, i, j):
    matrice[i], matrice[j] = matrice[j], matrice[i]

def transvection(matrice, k, i, alpha):
    ligne_modifiee = [matrice[k][j] - alpha * matrice[i][j] for j in range(len(matrice[k]))]
    matrice[k] = ligne_modifiee

def gauss_jordan(matrice):
    n = len(matrice)
    m = len(matrice[0])
    r = -1

    for j in range(m):
        max_val = 0
        max_index = -1

        for i in range(r + 1, n):
            if abs(matrice[i][j]) > max_val:
                max_val = abs(matrice[i][j])
                max_index = i

        if max_index == -1:
            continue

        r += 1
        pivot = matrice[max_index][j]

        for k in range(m):
            matrice[max_index][k] /= pivot

        if max_index != r:
            inverse_lignes(matrice, max_index, r)

        for i in range(n):
            if i != r:
                coeff = matrice[i][j]
                transvection(matrice, i, r, coeff)

    return matrice

def main():
    while True:
        n = int(input("Entrez le nombre de variables : "))
        m = int(input("Entrez le nombre d'équations : "))

        if n != m:
            print("Le nombre de variables et d'équations doit être le même.")
            continue
        else:
            break

    print("Entrez les coefficients du système d'équations :")
    A = creer_matrice(m, n)

    print("\nMatrice des coefficients du système d'équations :")
    for ligne in A:
        print(ligne)

    print("\nMatrice inverse :")
    A_inverse = gauss_jordan(A)
    for ligne in A_inverse:
        print(ligne)

    print("\nEntrez les termes constants du système d'équations, séparés par des espaces :")
    b = [float(x) for x in input().split()]

    print("\nVecteur des termes constants :")
    print(b)

    print("\nSolutions du système d'équations :")
    solutions = [sum(x * y for x, y in zip(ligne, b)) for ligne in A_inverse]
    for i, solution in enumerate(solutions, 1):
        print(f"x{i} =", solution)

if __name__ == "__main__":
    main()
