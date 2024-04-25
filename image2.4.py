import tkinter as tk
from PIL import Image, ImageTk

# Initialiser la fenêtre principale de Tkinter avant tout
root = tk.Tk()
root.title("LABO COURS DE MATH: TRAITEMENT D'IMAGES")

def create_mirror_image(image_path):
    original_image = Image.open(image_path)
    # Appliquer l'effet miroir à l'image
    width, height = original_image.size
    mirror_image = original_image.transpose(Image.FLIP_LEFT_RIGHT)
    return original_image, mirror_image

# Chemin vers l'image originale
image_path = 'C:/Users/abde/OneDrive/Bureau/Math/Lenna512.png'

# Créer l'image miroir et charger l'image originale
original_image, mirror_image = create_mirror_image(image_path)

# Convertir les images PIL en images Tkinter après l'initialisation de la fenêtre Tkinter
original_photo = ImageTk.PhotoImage(original_image)
mirror_photo = ImageTk.PhotoImage(mirror_image)

# Affichage de l'image originale
original_label = tk.Label(root, image=original_photo)
original_label.pack(side="top", pady=10)
original_text = tk.Label(root, text="Image avant transformation")
original_text.pack(side="top")

# Affichage de l'image miroir
mirror_label = tk.Label(root, image=mirror_photo)
mirror_label.pack(side="top", pady=10)
mirror_text = tk.Label(root, text="Image après transformation")
mirror_text.pack(side="top")

# Bouton pour quitter l'application
quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="bottom", pady=10)

# Exécution de la boucle principale
root.mainloop()
