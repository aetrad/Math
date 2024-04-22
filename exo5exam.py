import numpy as np
from collections import Counter
import re

# Message donné
message = """
Þjálfun gerð fyrir þig Tölvunarfræðibrautin þróar, einn eða sem hluti af hópi sérfræðinga, greiningarskrá fyrir verkefni. Hann forritar forrit, sér um viðhald þeirra og tekur þátt í þjálfun notenda. Hann leysir, einn eða með aðstoð sérfræðings, vandamál sem tengjast stýrikerfisumhverfi, staðarnetum eða fjarskiptakerfum. Fjölhæfur, veitir notendastuðning og er kjarninn í vandamálum varðandi notendavænni og framleiðni tölvukerfa. Hann tekur að sér stjórn vélagarðsins. Við núverandi skortsástand fær stúdentinn í tölvunarfræði atvinnu í námi sínu sem tölvusérfræðingur á öllum sviðum. By Jove Good luck !
"""

# Nettoyage et préparation du message pour analyse
message = re.sub(r'[^a-zA-ZÞðáéíóúýþæö]', '', message)  # inclure des caractères islandais
message_freq = Counter(message.lower())
total_letters = sum(message_freq.values())
message_freq_vector = np.array([message_freq.get(chr(i), 0) / total_letters for i in range(ord('a'), ord('z')+1)] + [message_freq.get(ch, 0) / total_letters for ch in 'Þðáéíóúýþæö'])

# Matrice de fréquences de lettres pour les différentes langues (à définir)
# Supposons que matrice2 est une matrice correctement définie avec des fréquences pour chaque langue
matrice2 = # [Votre matrice de données ici]

# Calcul des distances euclidiennes
distances = np.sqrt(np.sum((matrice2 - message_freq_vector.reshape(1, -1)) ** 2, axis=1))

# Détermination de la langue avec la distance minimale
language_index = np.argmin(distances)
languages = ['Anglais', 'Français', 'Allemand', 'Espagnol', 'Portugais', 'Espéranto', 'Italien', 'Turc', 'Suédois', 'Polonais', 'Néerlandais', 'Danois', 'Islandais', 'Finnois', 'Tchèque', 'Lituanien']
print(f"La langue la plus probable est : {languages[language_index]}")
