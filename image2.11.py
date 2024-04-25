import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

def adjust_contrast(image_path):
    # Charger l'image originale
    original_image = Image.open(image_path)
    # Convertir en un tableau NumPy
    image_data = np.array(original_image)
    
    # Calculer l'intensité pour chaque pixel
    intensity = image_data.mean(axis=2)
    i_min, i_max = intensity.min(), intensity.max()

    # Éviter la division par zéro dans le cas où l'image a une plage d'intensité nulle
    if i_max == i_min:
        return original_image
    
    # Calculer la nouvelle intensité normalisée
    scale = 255.0 / (i_max - i_min)
    new_intensity = scale * (intensity - i_min)
    
    # Mettre à jour les couleurs des pixels
    new_image_data = (scale * (image_data - i_min)).clip(0, 255).astype(np.uint8)
    
    # Convertir le tableau modifié en image PIL
    contrast_image = Image.fromarray(new_image_data)
    return contrast_image

# Chemin vers l'image originale
image_path = 'Lenna512.png'  # Remplacez par le chemin de votre fichier image

# Modifier le contraste
contrast_image = adjust_contrast(image_path)

# Initialiser la fenêtre Tkinter
root = tk.Tk()
root.title("Modification du contraste")

# Convertir l'image contrastée PIL en image Tkinter
contrast_photo = ImageTk.PhotoImage(contrast_image)

# Afficher l'image à contraste modifié
contrast_label = tk.Label(root, image=contrast_photo)
contrast_label.pack(side="top", pady=10)
contrast_text = tk.Label(root, text="Image à contraste modifié")
contrast_text.pack(side="top")

# Bouton pour quitter l'application
quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="bottom", pady=10)

# Exécution de la boucle principale
root.mainloop()
