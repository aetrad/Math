# Définition de la matrice M
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Affichage de la matrice M
print("Matrice M :")
for row in M:
    print(row)

# Affichage de l'élément m23 (élément de la ligne 2, colonne 3)
print("Élément m23 :", M[1][2])  # Indices commencent à 0

# Affichage de la 3ème ligne
print("3ème ligne :", M[2])

# Affichage de la première colonne
first_column = [row[0] for row in M]  # Utilisation d'une compréhension de liste
print("Première colonne :", first_column)
