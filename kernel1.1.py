import numpy as np
from scipy.signal import convolve2d

def custom_convolve(image, kernel):
    """
    Applique une convolution entre une image et un kernel spécifié.

    Args:
    image (np.array): Matrice représentant l'image à traiter.
    kernel (np.array): Matrice représentant le kernel de convolution.

    Returns:
    np.array: Image résultante après convolution.
    """
    # Appliquer la convolution en utilisant 'same' pour conserver la dimension de l'image originale
    result = convolve2d(image, kernel, mode='same', boundary='wrap')
    return result

# Exemple d'utilisation
if __name__ == "__main__":
    # Création d'une image exemple (matrice) et d'un kernel de convolution
    image = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

    # Appel de la fonction custom_convolve
    convoluted_image = custom_convolve(image, kernel)
    print("Image après convolution :")
    print(convoluted_image)
