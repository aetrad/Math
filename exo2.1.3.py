import numpy as np

# Définir les arrays A et B
A = np.array([[4.1, 2.0, 0], [4.6, 1, 6], [2, 8, 3]])
B = np.array([[1, 1, 0], [1.0, 1, 1], [2, 2, 2]])

# Afficher les matrices A et B
print("Array A:")
print(A)

print("Array B:")
print(B)

# Calculer et afficher A+B
AB = A + B
print("Résultat de l'addition A + B:")
print(AB)
