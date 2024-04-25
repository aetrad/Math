import tkinter as tk
from PIL import Image, ImageTk

# Fonction pour convertir une image en négatif
def convert_to_negative(image_path):
    # Charger l'image
    original_image = Image.open(image_path)
    # Convertir l'image en négatif
    negative_image = Image.eval(original_image, lambda v: 255 - v)
    return original_image, negative_image

# Chemin vers l'image originale
image_path = 'Lenna512.png'  # Remplacez par le chemin de votre fichier image

# Convertir l'image en négatif et charger l'image originale
original_image, negative_image = convert_to_negative(image_path)

# Initialiser la fenêtre Tkinter
root = tk.Tk()
root.title("LABO COURS DE MATH: TRAITEMENT D'IMAGES")

# Convertir les images PIL en images Tkinter
original_photo = ImageTk.PhotoImage(original_image)
negative_photo = ImageTk.PhotoImage(negative_image)

# Afficher l'image originale
original_label = tk.Label(root, image=original_photo)
original_label.pack(side="top", pady=10)
original_text = tk.Label(root, text="Image avant transformation")
original_text.pack(side="top")

# Afficher l'image en négatif
negative_label = tk.Label(root, image=negative_photo)
negative_label.pack(side="top", pady=10)
negative_text = tk.Label(root, text="Image après transformation")
negative_text.pack(side="top")

# Bouton pour quitter l'application
quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="bottom", pady=10)

# Exécution de la boucle principale
root.mainloop()
