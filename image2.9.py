import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

def mix_images(image_path1, image_path2, alpha):
    # Charger les images
    image1 = Image.open(image_path1)
    image2 = Image.open(image_path2)

    # Convertir les images en tableaux NumPy
    image1_data = np.array(image1)
    image2_data = np.array(image2)

    # Mélanger les deux images
    mixed_image_data = alpha * image1_data + (1 - alpha) * image2_data
    # Assurer que les données sont de type uint8 et ne dépassent pas 255
    mixed_image_data = np.clip(mixed_image_data, 0, 255).astype(np.uint8)
    mixed_image = Image.fromarray(mixed_image_data)

    return mixed_image

# Chemins vers les images
image_path1 = 'Lenna512.png'  # Remplacez par le chemin de votre première image
image_path2 = '4-2-03.png'  # Remplacez par le chemin de votre seconde image

# Proportion du mélange
alpha = 0.6  # 60% de la première image et 40% de la seconde

# Mélanger les images
mixed_image = mix_images(image_path1, image_path2, alpha)

# Initialiser la fenêtre Tkinter
root = tk.Tk()
root.title("Mixage de deux images")

# Convertir l'image mélangée PIL en image Tkinter
mixed_photo = ImageTk.PhotoImage(mixed_image)

# Afficher l'image mélangée
mixed_label = tk.Label(root, image=mixed_photo)
mixed_label.pack(side="top", pady=10)
mixed_text = tk.Label(root, text="Image mélangée")
mixed_text.pack(side="top")

# Bouton pour quitter l'application
quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="bottom", pady=10)

# Exécution de la boucle principale
root.mainloop()
