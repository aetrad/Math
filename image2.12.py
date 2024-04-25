import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

# Fonction pour redimensionner une image avec la méthode du plus proche voisin
def resize_image_nearest(image_path, new_size):
    # Charger l'image originale
    original_image = Image.open(image_path)
    # Obtenir les dimensions originales
    original_size = original_image.size

    # Calculer les ratios de transformation
    ratio_lignes = original_size[1] / new_size[1]
    ratio_colonnes = original_size[0] / new_size[0]

    # Créer un tableau NumPy pour la nouvelle image
    new_image_data = np.zeros((new_size[1], new_size[0], 3), dtype=np.uint8)

    # Remplir la nouvelle image
    for ligne in range(new_size[1]):
        for col in range(new_size[0]):
            # Trouver les coordonnées correspondantes dans l'image originale
            original_ligne = int(ligne * ratio_lignes)
            original_col = int(col * ratio_colonnes)
            # Copier la couleur du pixel
            new_image_data[ligne, col] = original_image.getpixel((original_col, original_ligne))

    # Convertir le tableau NumPy en image PIL
    resized_image = Image.fromarray(new_image_data)
    return resized_image

# Chemins vers l'image originale et l'image redimensionnée
original_image_path = 'Lenna512.png'  # Remplacez par le chemin de votre fichier image

# Nouvelles dimensions souhaitées
new_size = (220, 220)

# Redimensionner l'image
resized_image = resize_image_nearest(original_image_path, new_size)

# Initialiser la fenêtre Tkinter
root = tk.Tk()
root.title("Redimensionner une image")

# Convertir l'image redimensionnée PIL en image Tkinter
resized_photo = ImageTk.PhotoImage(resized_image)

# Afficher l'image redimensionnée
resized_label = tk.Label(root, image=resized_photo)
resized_label.pack(side="top", pady=10)
resized_text = tk.Label(root, text="Image redimensionnée")
resized_text.pack(side="top")

# Bouton pour quitter l'application
quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="bottom", pady=10)

# Exécution de la boucle principale
root.mainloop()
