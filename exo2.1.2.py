# Définir les matrices A et B
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 9, 9], [9, 9, 9], [9, 9, 9]]

# Afficher les matrices A et B
print("Matrice A:")
for row in A:
    print(row)

print("Matrice B:")
for row in B:
    print(row)

# Addition simple des listes (non matricielle)
AB_concat = A + B
print("Résultat de l'addition simple (concaténation) de A et B:")
print(AB_concat)

# Addition matricielle de A et B
AB_matricielle = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print("Résultat de l'addition matricielle de A et B:")
for row in AB_matricielle:
    print(row)
