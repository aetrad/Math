import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

def isolate_color_component(image_path, color_component):
    # Charger l'image originale
    original_image = Image.open(image_path)
    # Convertir en un tableau NumPy
    image_data = np.array(original_image)
    
    # Isoler la composante de couleur
    if color_component == 'red':
        mask = np.array([1, 0, 0])
    elif color_component == 'green':
        mask = np.array([0, 1, 0])
    elif color_component == 'blue':
        mask = np.array([0, 0, 1])
    else:
        raise ValueError("Invalid color component")

    # Appliquer le masque pour garder seulement la composante souhaitée
    isolated_image_data = (image_data * mask).astype(np.uint8)
    isolated_image = Image.fromarray(isolated_image_data)
    
    return original_image, isolated_image

# Chemin vers l'image originale
image_path = 'Lenna512.png'  # Remplacez par le chemin de votre fichier image

# Isoler la composante de couleur (red, green, blue)
original_image, isolated_image = isolate_color_component(image_path, 'red')  # Exemple pour isoler le rouge

# Initialiser la fenêtre Tkinter
root = tk.Tk()
root.title("LABO COURS DE MATH: TRAITEMENT D'IMAGES")

# Convertir les images PIL en images Tkinter
original_photo = ImageTk.PhotoImage(original_image)
isolated_photo = ImageTk.PhotoImage(isolated_image)

# Afficher l'image originale
original_label = tk.Label(root, image=original_photo)
original_label.pack(side="top", pady=10)
original_text = tk.Label(root, text="Image avant transformation")
original_text.pack(side="top")

# Afficher l'image avec la composante de couleur isolée
isolated_label = tk.Label(root, image=isolated_photo)
isolated_label.pack(side="top", pady=10)
isolated_text = tk.Label(root, text="Image après transformation")
isolated_text.pack(side="top")

# Bouton pour quitter l'application
quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="bottom", pady=10)

# Exécution de la boucle principale
root.mainloop()
