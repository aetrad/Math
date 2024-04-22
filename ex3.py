#-*- coding: utf8 -*-

# La première ligne indique le type d'encodage utilisé.

#----------------------------------------------------------------------#
#                                                                      #
#             Cours de Mathématiques pour BAC Info chap. 2             #
#                         Traitement d'images                          #
#                            G. Barmarin                               #
#                             2021-2022                                #
#                                                                      #
#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
#                                                                      #
#                           Ex 2.3 Enoncé                              #
#                                                                      #
#                        Rognage d'une image                           #                                                          
#                                                                      #
#----------------------------------------------------------------------#

#-----------------------------------------------------------------------
# Importation des bibliothèques
#-----------------------------------------------------------------------

import time
from tkinter import *
from PIL import Image, ImageTk
import numpy as np 

#-----------------------------------------------------------------------
# encodage des fonctions 
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
# encodage du programme principal
#-----------------------------------------------------------------------

print("Utilisation de numpy et de PIL")
print("------------------------------")
print("Utilisation des arrays pour traiter des images\n")

# On charge l'image et on la transforme en tableau (dé-commenter le format qui vous intéresse)

nom="images/Lenna512.png"

start = time.time()			# stocke l'heure du démarrage du traitement

image_entree = Image.open(nom)
image = np.asarray(image_entree)
nb_lignes = image.shape[0]
nb_colonnes = image.shape[1]

#-----------------------------------------------------------------------
# Traitement de l'image
#-----------------------------------------------------------------------

# Crop de l'image

a=240		# début en hauteur du crop
b=290		# fin en hauteur du crop
c=240		# début en largeur du crop
d=360		# fin en largeur du crop

# Vérifications des valeurs

if (0<=a<nb_lignes and a<b<=nb_lignes and 0<=c<nb_colonnes and c<d<=nb_colonnes)==False :
   print ("Ce n'est pas possible!")
   
# on ne garde que les lignes allant de a à b et les colonnes de c à d ce qui correspond au regard de Lenna...

image_sortie = image[a:b,c:d]

end = time.time()		# stocke l'heure de la fin du traitement

print("\nVous avez ouvert l'image ", nom)
print("qui a pour dimensions ", nb_lignes,"lignes et ", nb_colonnes, " colonnes\n")
print("Vous l'avez ensuite rognée pour ne garder que les colonnes de ", c , " à ", d, " et les lignes de ", a, " à ", b, "\n")
print(image)
print("\nEt voici ce que le tableau de sortie contient:\n")
print(image_sortie)
print("\n")
print ("Durée du traitement: ",end - start, " seconde\n")

# On sauvegarde les images pour pouvoir les afficher

Image.fromarray(image).save("image_entree.png")
Image.fromarray(image_sortie).save("image_sortie.png")

#-----------------------------------------------------------------------
# Affichage dans tkinter
#-----------------------------------------------------------------------

root=Tk()

empty_line0 = Label(root, text="")
empty_line0.pack()
empty_line00 = Label(root, text="LABO COURS DE MATH: TRAITEMENT D'IMAGES")
empty_line00.pack()
champ_label_result0 = Label(root, text="On affiche l'image avant transformation et après")
champ_label_result0.pack()
empty_line2 = Label(root, text="")
empty_line2.pack()

champ_label_result1 = Label(root, text="Image avant transformation")
champ_label_result1.pack() 
image_in = Image.open("image_entree.png")
photo = ImageTk.PhotoImage(image_in)

image_out = Image.open("image_sortie.png")
photo2 = ImageTk.PhotoImage(image_out)

canvas = Canvas(root,width=300,height=250,bg="silver")
canvas.create_image(150,127, image=photo)
canvas.pack()

champ_label_result2 = Label(root, text="Image après transformation")
champ_label_result2.pack() 

canvas = Canvas(root,width=300,height=250,bg="silver")
canvas.create_image(150,127, image=photo2)
canvas.pack()

empty_line3 = Label(root, text="")
empty_line3.pack()
bouton_valider = Button(root, text="Quit", command=root.destroy)
bouton_valider.pack()
empty_line4 = Label(root, text="")
empty_line4.pack()
root.mainloop()
