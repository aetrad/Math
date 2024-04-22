import numpy as np

# Matrice des commandes
A = np.array([
    [1, 2, 1, 0, 0],  # Commande 1
    [2, 1, 1, 1, 0],  # Commande 2
    [1, 0, 2, 2, 1],  # Commande 3
    [2, 2, 1, 1, 3],  # Commande 4
    [1, 0, 0, 2, 2]   # Commande 5
])

# Vecteur des coûts
b = np.array([55, 65.5, 80, 117.5, 63.5])

# Résolution du système d'équations linéaires pour trouver les prix des pizzas
prix_pizzas = np.linalg.lstsq(A, b, rcond=None)[0]

# Affichage des prix
types_pizzas = ["Margherita", "Quatre-saisons", "Végétarienne", "Hawaïenne", "Napolitaine"]
for pizza, prix in zip(types_pizzas, prix_pizzas):
    print(f"Prix de la pizza {pizza} : {prix:.2f} €")
