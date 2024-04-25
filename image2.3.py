import tkinter as tk
from PIL import Image, ImageTk

def crop_region(image_path, start_row, end_row, start_col, end_col):
    image = Image.open(image_path)
    return image.crop((start_col, start_row, end_col, end_row))

# Chemin vers l'image originale
image_path = 'Lenna512.png'  # Remplacez ceci par le chemin vers votre image Lenna

# Coordonnées pour le recadrage
start_row, end_row = 240, 290
start_col, end_col = 240, 360

# Création de la fenêtre Tkinter
root = tk.Tk()
root.title("LABO COURS DE MATH: TRAITEMENT D'IMAGES")

# Charger l'image originale et la région d'intérêt
original_image = Image.open(image_path)
roi_image = crop_region(image_path, start_row, end_row, start_col, end_col)

# Convertir les images PIL en images Tkinter
original_photo = ImageTk.PhotoImage(original_image)
roi_photo = ImageTk.PhotoImage(roi_image)

# Afficher l'image originale
original_label = tk.Label(root, image=original_photo)
original_label.pack()

# Ajouter un texte pour indiquer la transformation
transform_text = tk.Label(root, text="Image après transformation")
transform_text.pack()

# Afficher la région d'intérêt
roi_label = tk.Label(root, image=roi_photo)
roi_label.pack()

# Bouton pour quitter l'application
quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.pack()

# Exécution de la boucle principale
root.mainloop()
