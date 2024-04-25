import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

# Chemin vers l'image originale
image_path = '4-2-03.png'  # Remplacez par le chemin de votre fichier image

# Fonction pour isoler les zones en fonction d'un seuil de la composante rouge
def isolate_color_threshold(image_path, threshold):
    # Charger l'image originale
    original_image = Image.open(image_path)
    # Convertir en un tableau NumPy
    image_data = np.array(original_image)
    
    # Isoler les zones où la composante rouge dépasse le seuil
    mask = image_data[:, :, 0] < threshold
    image_data[mask] = [0, 0, 0]  # Zones en dessous du seuil passent en noir
    image_data[~mask] = [255, 255, 255]  # Zones au-dessus du seuil, changer selon l'envie

    # Convertir le tableau modifié en image PIL
    threshold_image = Image.fromarray(image_data)
    return original_image, threshold_image

# Appliquer le seuil pour isoler les zones
original_image, threshold_image = isolate_color_threshold(image_path, 220)

# Initialiser la fenêtre Tkinter
root = tk.Tk()
root.title("LABO COURS DE MATH: TRAITEMENT D'IMAGES")

# Convertir les images PIL en images Tkinter
original_photo = ImageTk.PhotoImage(original_image)
threshold_photo = ImageTk.PhotoImage(threshold_image)

# Afficher l'image originale
original_label = tk.Label(root, image=original_photo)
original_label.pack(side="top", pady=10)
original_text = tk.Label(root, text="Image avant transformation")
original_text.pack(side="top")

# Afficher l'image avec le seuil appliqué
threshold_label = tk.Label(root, image=threshold_photo)
threshold_label.pack(side="top", pady=10)
threshold_text = tk.Label(root, text="Image après transformation")
threshold_text.pack(side="top")

# Bouton pour quitter l'application
quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="bottom", pady=10)

# Exécution de la boucle principale
root.mainloop()
