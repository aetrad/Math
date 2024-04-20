# Définition de la matrice M comme une liste de listes
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Afficher la liste de listes (la matrice M)
print("Matrice M :")
for ligne in M:
    print(ligne)

# Afficher l'élément m23 (3ème élément de la 2ème ligne, en considérant une indexation à partir de 1)
print("\nÉlément m23 :", M[1][2])  # Souvenez-vous que l'indexation en Python commence à 0

# Afficher la 3ème ligne de la matrice
print("\n3ème ligne :", M[2])

# Afficher la première colonne de la matrice
# Utilisation d'une compréhension de liste pour extraire le premier élément de chaque ligne
premiere_colonne = [ligne[0] for ligne in M]
print("\nPremière colonne :", premiere_colonne)
