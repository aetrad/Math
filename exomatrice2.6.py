import numpy as np

def calculer_prix_pizzas():
    # Matrice des coefficients correspondant aux quantités de chaque type de pizza commandée
    A = np.array([
        [1, 2, 1, 0, 0],  # 1 Margherita, 2 Quatre-saisons, 1 Végétarienne
        [2, 1, 1, 1, 0],  # 2 Margherita, 1 Quatre-saisons, 1 Végétarienne, 1 Hawaïenne
        [1, 0, 2, 2, 1],  # 1 Margherita, 2 Hawaïenne, 2 Végétarienne, 1 Napolitaine
        [2, 2, 1, 1, 3],  # 2 Margherita, 2 Quatre-saisons, 1 Végétarienne, 1 Hawaïenne, 3 Napolitaine
        [1, 0, 0, 2, 2]   # 1 Margherita, 2 Hawaïenne, 2 Napolitaine
    ])
    
    # Vecteur des totaux payés pour chaque commande
    b = np.array([55, 65.5, 80, 117.5, 63.5])
    
    # Résolution du système linéaire pour trouver les prix de chaque type de pizza
    prix_pizzas = np.linalg.solve(A, b)
    
    return prix_pizzas

# Exécuter la fonction et imprimer les résultats
prix = calculer_prix_pizzas()
noms_pizzas = ["Margherita", "Quatre-saisons", "Végétarienne", "Hawaïenne", "Napolitaine"]
for nom, prix_pizza in zip(noms_pizzas, prix):
    print(f"Le prix de la pizza {nom} est de {prix_pizza:.2f} €")

