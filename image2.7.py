import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

# Fonction pour convertir une image en nuances de gris selon la luminance
def convert_to_grayscale(image_path):
    # Charger l'image originale
    original_image = Image.open(image_path)
    # Convertir en un tableau NumPy
    image_data = np.array(original_image)
    
    # Calculer la luminance
    luminance = 0.2126 * image_data[:, :, 0] + 0.7152 * image_data[:, :, 1] + 0.0722 * image_data[:, :, 2]
    luminance = luminance.astype(np.uint8)
    
    # Créer une image en nuances de gris
    grayscale_image_data = np.stack((luminance,)*3, axis=-1)
    grayscale_image = Image.fromarray(grayscale_image_data)
    
    return original_image, grayscale_image

# Chemin vers l'image originale
image_path = 'Lenna512.png'  # Remplacez par le chemin de votre fichier image

# Convertir l'image en nuances de gris
original_image, grayscale_image = convert_to_grayscale(image_path)

# Initialiser la fenêtre Tkinter
root = tk.Tk()
root.title("LABO COURS DE MATH: TRAITEMENT D'IMAGES")

# Convertir les images PIL en images Tkinter
original_photo = ImageTk.PhotoImage(original_image)
grayscale_photo = ImageTk.PhotoImage(grayscale_image)

# Afficher l'image originale
original_label = tk.Label(root, image=original_photo)
original_label.pack(side="top", pady=10)
original_text = tk.Label(root, text="Image avant transformation")
original_text.pack(side="top")

# Afficher l'image en nuances de gris
grayscale_label = tk.Label(root, image=grayscale_photo)
grayscale_label.pack(side="top", pady=10)
grayscale_text = tk.Label(root, text="Image après transformation")
grayscale_text.pack(side="top")

# Bouton pour quitter l'application
quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="bottom", pady=10)

# Exécution de la boucle principale
root.mainloop()
