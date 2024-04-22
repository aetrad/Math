#-*- coding: utf8 -*-

########################################################################
'''
  _   __    _   _____  _   _                         _   _
 |  \/  |  /_\ |_   _|| |_| | (_) _  _   ____  _  _ | |_| |_   ___  _ _
 | |\/| | / _ \  | |  |  _  | | || \| | |  _ \| || ||  _| _ \ / _ \| \ |
 |_|  |_|/_/ \_\ |_|  |_| |_| |_||_|\_| |  __/\_, /  \__|_||_|\___/|_\_|
                                        |_|   |__/
'''
########################################################################

#-----------------------------------------------------------------------
#                                                          
#                       Project Math-BacInfo-Python                     
#                             Template Python                     
#                              G. Barmarin                         
#                                                         
#                               2022-2023                          
#                                                          
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#                         Source: Gérard Barmarin                       
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#                         Que fait ce programme?                                 
#-----------------------------------------------------------------------

# Ce progamme reprend les exercices de traitement d'images partie 1

#-----------------------------------------------------------------------
#                      Importation des librairies                       
#-----------------------------------------------------------------------

#import csv
import time
#import sys
#import os
import numpy as np
#import numpy.linalg as alg
#import PIL
from PIL import Image, ImageTk											
import tkinter as tk
#import colorsys
#import matplotlib
import matplotlib.pyplot as plt
import scipy
from scipy.ndimage import convolve
from scipy import signal
#import cv2
#import skimage
#import sklearn
#import pandas
#import webcolors

#-----------------------------------------------------------------------
# encodage des fonctions 
#-----------------------------------------------------------------------



#-----------------------------------------------------------------------
#              Définition / initialisation des variables               
#-----------------------------------------------------------------------



#-----------------------------------------------------------------------
# encodage du programme principal
#-----------------------------------------------------------------------

print("\n---------------------------------------------\n")

# Ouverture de l'image et mise dans une matrice/tableau numpy

image_directory = "images"												# les répertoires doivent exister
image_mod_directory = "images_mod"										# les répertoires doivent exister
image_name ="Lenna512"													# 4-2-03 ou Lenna512
image_extension = "png"													# ou png, bmp, gif
print("\nOuverture avec numpy de l'image", image_name+"."+image_extension,"se trouvant dans le répertoire", image_directory+"/", "\n et stockage dans un tableau numpy\n")
mon_image = Image.open( image_directory+"/"+image_name+"."+image_extension ) #ouverture de l'image avec le module Image de PIL
mon_image_array = np.array( mon_image )									# l'image est placée dans un tableau numpy
matrice_img_array = np.array( mon_image )	
print( 'classe :', type(matrice_img_array) )							# dont on peut demander les caractéristiques
print( 'type :', matrice_img_array.dtype )
print( 'taille :', matrice_img_array.shape )
print(matrice_img_array.size,'pixels')
print( 'Largeur de l\'image :', matrice_img_array.shape[1] )
print( 'Hauteur de l\'image :', matrice_img_array.shape[0] )
print( 'Valeur RGB du pixel (3,511): ',matrice_img_array[250,250,:])
print("\n---------------------------------------------\n")
largeur = matrice_img_array.shape[1]
hauteur = matrice_img_array.shape[0]
matrice_img_array_mod = np.copy(matrice_img_array)						# copie du tableau de l'image originale dans un nouveau tableau de travail
matrice_R = matrice_img_array[:,:,0]									# Extraction de la couche Rouge dans une matrice nxp à 2 dimensions
matrice_G = matrice_img_array[:,:,1]									# Extraction de la couche Vertee dans une matrice nxp à 2 dimensions
matrice_B = matrice_img_array[:,:,2]									# Extraction de la couche Bleue dans une matrice nxp à 2 dimensions

#Traitement des couches: transposition (rotation vers la gauche de 90°)
'''
#matrice_img_array_mod [:,:,0] = matrice_R.T
#matrice_img_array_mod [:,:,1] = matrice_G.T
#matrice_img_array_mod [:,:,2] = matrice_B.T

# Reflet horizontal
matrice_img_array_mod [:,:,0] = np.flip(matrice_R,0)
matrice_img_array_mod [:,:,1] = np.flip(matrice_G,0)
matrice_img_array_mod [:,:,2] = np.flip(matrice_B,0)
# reflet vertical
matrice_img_array_mod [:,:,0] = np.flip(matrice_R,1)
matrice_img_array_mod [:,:,1] = np.flip(matrice_G,1)
matrice_img_array_mod [:,:,2] = np.flip(matrice_B,1)
'''

#Traitement des couches: couche bleue
'''
# Affichage en N&B
matrice_img_array_mod [:,:,0] = matrice_B
matrice_img_array_mod [:,:,1] = matrice_B
matrice_img_array_mod [:,:,2] = matrice_B
# Affichage en bleu
matrice_img_array_mod [:,:,0] = 0
matrice_img_array_mod [:,:,1] = 0
matrice_img_array_mod [:,:,2] = matrice_B
'''

#Traitement des couches: négatif
'''
M255 = 255*np.ones( (matrice_img_array.shape[0], matrice_img_array.shape[1]) )
#print (M255)
matrice_img_array_mod [:,:,0] = M255 - matrice_R 
matrice_img_array_mod [:,:,1] = M255 - matrice_G 
matrice_img_array_mod [:,:,2] = M255 - matrice_B 
'''
'''
# Image en niveau de gris 
'''
a = 0.2126
b = 0.7152
c = 0.0722
matrice_img_array_mod [:,:,0] = a*matrice_R + b*matrice_G + c*matrice_B
matrice_img_array_mod [:,:,1] = matrice_img_array_mod [:,:,0]
matrice_img_array_mod [:,:,2] = matrice_img_array_mod [:,:,0]

plt.imshow(matrice_img_array_mod)   # affiche la matrice de triplets RVB
plt.show() # ouvre la fenêtre d’affichage et attend la fin de l’interaction utilisateur

'''
a = 0.2126
b = 0.7152
c = 0.0722
matrice_img_array_mod = a*matrice_R + b*matrice_G + c*matrice_B
'''

# Image en sépia (manque clip)
'''
matrice_RS = 0.393*matrice_R + 0.769*matrice_G + 0.189*matrice_B
matrice_GS = 0.349*matrice_R + 0.686*matrice_G + 0.168*matrice_B
matrice_BS = 0.272*matrice_R + 0.534*matrice_G + 0.131*matrice_B
matrice_img_array_mod [:,:,0] = np.where(matrice_RS<=255,matrice_RS,255)
matrice_img_array_mod [:,:,1] = np.where(matrice_GS<=255,matrice_GS,255)
matrice_img_array_mod [:,:,2] = np.where(matrice_BS<=255,matrice_BS,255)
'''

# Contraste assombrir
'''
Cmin = np.amin(matrice_img_array)
Cmax = np.amax(matrice_img_array) 
print("min:",Cmin,"Max:",Cmax)
seuil = 100
matrice_img_array_mod = np.where(matrice_img_array<seuil,0,matrice_img_array-seuil)

#matrice_R = np.where(matrice_R<seuil,0,matrice_R-seuil)
#matrice_G = np.where(matrice_G<seuil,0,matrice_G-seuil)
#matrice_B = np.where(matrice_B<seuil,0,matrice_B-seuil)
#matrice_R = np.where(matrice_R>245,255,matrice_R)
#matrice_G = np.where(matrice_G>245,255,matrice_G)
#matrice_B = np.where(matrice_B>245,255,matrice_B)
#matrice_R = np.where(30<matrice_R<245,: int(round((255.0/195.0) * (c - 30) + 0.5)),matrice_R)
#matrice_G = np.where(matrice_G>245,255,matrice_G)
#matrice_B = np.where(matrice_B>245,255,matrice_B)
'''

# Contraste éclaircir
'''
Cmin = np.amin(matrice_img_array)
Cmax = np.amax(matrice_img_array) 
print("min:",Cmin,"Max:",Cmax)
seuil = 160
matrice_img_array_mod = np.where(matrice_img_array>seuil,255,matrice_img_array+255-seuil)
'''

# Contraste incomplet
'''
Cmin = min(matrice_img_array)
Cmax = max(matrice_img_array) 
matrice_R = np.where(matrice_R<30,0,matrice_R)
matrice_G = np.where(matrice_G<30,0,matrice_G)
matrice_B = np.where(matrice_B<30,0,matrice_B)
matrice_R = np.where(matrice_R>245,255,matrice_R)
matrice_G = np.where(matrice_G>245,255,matrice_G)
matrice_B = np.where(matrice_B>245,255,matrice_B)
#matrice_R = np.where(30<matrice_R<245,: int(round((255.0/195.0) * (c - 30) + 0.5)),matrice_R)
#matrice_G = np.where(matrice_G>245,255,matrice_G)
#matrice_B = np.where(matrice_B>245,255,matrice_B)
'''
# Mélange de 2 images
'''
matrice_img2 = Image.open("images/Lenna512.jpg" ) 						# ouverture de la deuxième image avec le module Image de PIL
matrice_img_array2 = np.array( matrice_img2 )	
alpha=0.4																# si alpha = 1 on obtient l'image 1 seule s'il vaut 0 on obtient l'image 2 seule
matrice_img_array_mod  = alpha*matrice_img_array + (1 - alpha)*matrice_img_array2
print(matrice_img_array_mod)
matrice_img_array_mod = np.asarray(matrice_img_array_mod ,dtype = int)	# repasser en entier int8? 0,999-alpha?
'''

# Crop 
'''
l1 = 240
l2 = 290
h1 = 240
h2 = 360
#l = abs(l2-l1)
#h = abs(h2-h1)
# création de la matrice de réception
MC = matrice_img_array[l1-1:l2-1, h1-1:h2-1]# crop
plt.imshow(MC) 
'''

# Test Convolution
'''
M = [[1,0,2],[2,1,0],[1,0,3]]
T = [[2,1,3,0],[1,1,0,5],[3,3,1,0],[2,0,0,2]]
C=signal.convolve2d(T, M, mode='same', boundary='fill', fillvalue=0)
D=convolve(T, M)
print(D,C)
'''
'''
# Essai de filtre
'''
#M = [[1,2,1],[2,4,2],[1,2,1]]
F = [[1/9, 1/9,1/9],[1/9, 1/9,1/9],[1/9, 1/9,1/9]]
#M = [[0,2,0],[2,-8,2],[0,2,0]] # contour1
M = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]] # contour2
matrice_img_array_mod2 = np.copy(matrice_img_array_mod)	
matrice_img_array_mod2 [:,:,0]=signal.convolve2d(matrice_img_array_mod [:,:,0], F, mode='same', boundary='fill', fillvalue=0)
matrice_img_array_mod2 [:,:,0]=signal.convolve2d(matrice_img_array_mod2 [:,:,0], M, mode='same', boundary='fill', fillvalue=0)
matrice_img_array_mod = np.where(matrice_img_array_mod2 >255,255,matrice_img_array_mod2 )
matrice_img_array_mod [:,:,1]=matrice_img_array_mod2 [:,:,0]
matrice_img_array_mod [:,:,2]=matrice_img_array_mod2 [:,:,0]
M255 = 255*np.ones( (matrice_img_array.shape[0], matrice_img_array.shape[1]) )
matrice_img_array_mod [:,:,0] = M255 - matrice_img_array_mod [:,:,0] 
matrice_img_array_mod [:,:,1] = M255 - matrice_img_array_mod [:,:,1]
matrice_img_array_mod [:,:,2] = M255 - matrice_img_array_mod [:,:,2] 
print(matrice_img_array_mod [:,:,0])
matrice_img_array_mod = int(matrice_img_array_mod -255)
# Reconstitution du tableau correspondant à la nouvelle image RGB
'''
matrice_img_array_mod [:,:,0]= matrice_R
matrice_img_array_mod [:,:,1]= matrice_G
matrice_img_array_mod [:,:,2]= matrice_B
'''

plt.imshow(matrice_img_array_mod)   # affiche la matrice de triplets RVB
plt.show() # ouvre la fenêtre d’affichage et attend la fin de l’interaction utilisateur
