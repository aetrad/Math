# Définir les matrices A et B
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 9, 9], [9, 9, 9], [9, 9, 9]]

# Afficher les matrices A et B
print("Matrice A:")
for ligne in A:
    print(ligne)

print("\nMatrice B:")
for ligne in B:
    print(ligne)

# Addition de A et B comme listes (ceci ne donnera pas le résultat attendu)
print("\nAddition de A et B comme listes (non matriciel) :", A + B)

# Calcul et affichage de A+B selon les règles du calcul matriciel
somme = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print("\nAddition de A et B selon les règles du calcul matriciel :")
for ligne in somme:
    print(ligne)
