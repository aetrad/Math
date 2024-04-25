import numpy as np

def gauss_jordan_inverse(A):
    n = A.shape[0]
    if A.shape[0] != A.shape[1]:
        raise ValueError("La matrice doit être carrée pour être inversible.")
    
    # Créer la matrice augmentée [A | I]
    I = np.eye(n)
    A_aug = np.hstack([A, I])

    for j in range(n):
        # Recherche du pivot maximal dans la colonne j à partir de la ligne j
        max_row = np.argmax(np.abs(A_aug[j:, j])) + j
        if A_aug[max_row, j] == 0:
            raise ValueError("La matrice est singulière et ne peut être inversée.")
        
        # Échange des lignes si nécessaire
        A_aug[[j, max_row]] = A_aug[[max_row, j]]

        # Division de la ligne du pivot par le pivot
        A_aug[j] = A_aug[j] / A_aug[j, j]

        # Élimination des autres éléments de la colonne
        for i in range(n):
            if i != j:
                A_aug[i] = A_aug[i] - A_aug[i, j] * A_aug[j]
    
    # Extraction de la matrice inverse de la partie droite de la matrice augmentée
    return A_aug[:, n:]

def main():
    # Exemple d'utilisation
    A = np.array([
        [2, 1, 1],
        [1, 3, 2],
        [1, 0, 0]
    ], dtype=float)

    try:
        A_inv = gauss_jordan_inverse(A)
        print("La matrice inverse est :")
        print(A_inv)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
