import numpy as np

def saisir_systeme():
    while True:
        n = int(input("Combien y a-t-il de variables dans le système ? "))
        m = int(input("Combien y a-t-il d'équations dans le système ? "))
        
        if n != m:
            print("Erreur : le nombre de variables doit être égal au nombre d'équations pour un système déterminé.")
            continue
        
        # Création des matrices pour les coefficients et les termes constants
        A = np.zeros((m, n))
        b = np.zeros(m)
        
        # Saisie des coefficients de chaque équation
        for i in range(m):
            print(f"Saisissez les coefficients pour l'équation {i + 1}:")
            coefficients = list(map(float, input("Entrez les coefficients séparés par des espaces : ").split()))
            if len(coefficients) != n:
                print("Vous devez entrer exactement", n, "coefficients.")
                return None, None
            A[i] = coefficients
            b[i] = float(input("Entrez le terme constant de l'équation : "))
        
        return A, b

def resoudre_systeme(A, b):
    if A is None or b is None:
        return
    try:
        # Tentative de résolution du système d'équations
        solution = np.linalg.solve(A, b)
        print("Solution du système :")
        print(solution)
    except np.linalg.LinAlgError as e:
        print("Erreur lors de la résolution du système :", e)

def main():
    A, b = saisir_systeme()
    resoudre_systeme(A, b)

if __name__ == "__main__":
    main()
