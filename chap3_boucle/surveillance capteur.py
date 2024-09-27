import random

# Seuil critique pour les alertes
seuil_critique = 35.0
# Nombre de valeurs de température à générer
nombre_capteurs = 10

print("Collecte des données des capteurs :")

# Boucle pour générer et traiter les données
for i in range(nombre_capteurs):
    temperature = random.uniform(20, 40)
    
    if temperature > seuil_critique:
        print(f"ALERTE : Température élevée détectée : {temperature:.2f}°C")
    else:
        print(f"Température mesurée : {temperature:.2f}°C")
