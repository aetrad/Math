import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

# Fonction pour modifier la luminosité d'une image
def change_brightness(image_path, change):
    # Charger l'image originale
    original_image = Image.open(image_path)
    # Convertir en un tableau NumPy
    image_data = np.array(original_image)
    
    # Modifier la luminosité
    new_image_data = np.where((image_data + change) > 255, 255, np.where((image_data + change) < 0, 0, image_data + change))
    
    # Convertir le tableau modifié en image PIL
    brighter_image = Image.fromarray(new_image_data.astype(np.uint8))
    return original_image, brighter_image

# Chemin vers l'image originale
image_path = 'Lenna512.png'  # Remplacez par le chemin de votre fichier image

# Modifier la luminosité (exemple : augmenter de 30)
change = 30
original_image, brighter_image = change_brightness(image_path, change)

# Initialiser la fenêtre Tkinter
root = tk.Tk()
root.title("Modification de la luminosité")

# Convertir les images PIL en images Tkinter
original_photo = ImageTk.PhotoImage(original_image)
brighter_photo = ImageTk.PhotoImage(brighter_image)

# Afficher l'image originale
original_label = tk.Label(root, image=original_photo)
original_label.pack(side="top", pady=10)
original_text = tk.Label(root, text="Image originale")
original_text.pack(side="top")

# Afficher l'image à luminosité modifiée
brighter_label = tk.Label(root, image=brighter_photo)
brighter_label.pack(side="top", pady=10)
brighter_text = tk.Label(root, text="Image à luminosité modifiée")
brighter_text.pack(side="top")

# Bouton pour quitter l'application
quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="bottom", pady=10)

# Exécution de la boucle principale
root.mainloop()
