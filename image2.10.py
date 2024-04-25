import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

def green_screen_foreground(foreground_path, background_path, green_threshold):
    # Charger les images
    foreground = Image.open(foreground_path)
    background = Image.open(background_path).resize(foreground.size)
    
    # Convertir les images en tableaux NumPy
    foreground_data = np.array(foreground)
    background_data = np.array(background)
    
    # Déterminer où l'image du premier plan est verte (selon un seuil)
    # Cela suppose que le vert est plus présent que le rouge et le bleu
    is_green = np.where((foreground_data[:, :, 1] > green_threshold) &
                        (foreground_data[:, :, 1] > foreground_data[:, :, 0]) &
                        (foreground_data[:, :, 1] > foreground_data[:, :, 2]))
    
    # Remplacer le vert par le pixel du fond
    foreground_data[is_green] = background_data[is_green]
    
    # Convertir le tableau modifié en image PIL
    result_image = Image.fromarray(foreground_data)
    return result_image

# Chemins vers les images de premier plan (avec fond vert) et de fond
foreground_path = 'Lenna512.png'  # Remplacez par le chemin de votre image de premier plan
background_path = '4-2-03.png'  # Remplacez par le chemin de votre image de fond

# Seuil pour détecter le vert (ajustez selon votre image)
green_threshold = 150

# Appliquer l'effet de fond vert
result_image = green_screen_foreground(foreground_path, background_path, green_threshold)

# Initialiser la fenêtre Tkinter
root = tk.Tk()
root.title("Effet de fond vert")

# Convertir l'image résultante PIL en image Tkinter
result_photo = ImageTk.PhotoImage(result_image)

# Afficher l'image résultante
result_label = tk.Label(root, image=result_photo)
result_label.pack(side="top", pady=10)
result_text = tk.Label(root, text="Image avec fond vert remplacé")
result_text.pack(side="top")

# Bouton pour quitter l'application
quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="bottom", pady=10)

# Exécution de la boucle principale
root.mainloop()
