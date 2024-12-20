donnees_meteo = {
    "Paris": {"temperature": 20.0, "humidite": 60},
    "New York": {"temperature": 25.0, "humidite": 70},
    "Tokyo": {"temperature": 28.0, "humidite": 80}
}

def afficher_donnees_meteo(dictionnaire):

    print("Affichage des données météorologiques pour chaque ville:")
    for ville, meteo in dictionnaire.items():
        print(f"Ville : {ville}")
        print(f"Température : {meteo['temperature']}°C")
        print(f"Humidité : {meteo['humidite']}%\n")

def rechercher_donnees_meteo(dictionnaire):
    ville = input("Saisir le nom de la ville à rechercher: ")

    if ville in dictionnaire:
        print(f"Données météorologiques pour {ville}:")
        print(f"Température : {dictionnaire[ville]['temperature']}°C")
        print(f"Humidité : {dictionnaire[ville]['humidite']}%")
    else:
        print(f"Données météorologiques non disponibles pour {ville}.")

def mettre_a_jour_donnees_meteo(dictionnaire):
    ville = input("Saisir le nom de la ville à mettre à jour: ")
    if ville in dictionnaire:
        temperature= int(input("Sasir la nouvelle valeur de la température: "))
        humidite= int(input("Sasir la nouvelle valeur de l'humidité: "))
        dictionnaire[ville]["temperature"] = temperature
        dictionnaire[ville]["humidite"] = humidite
        print(f"Données météorologiques mises à jour pour {ville}.")
    else:
        print(f"Données météorologiques non disponibles pour {ville}.")



while True:
    choix = input("""
Que voulez vous faire?

1: afficher
2: rechercher
3: mettre à jour
4: quitter

> """)
    
    if choix =="1":
        afficher_donnees_meteo(donnees_meteo)

    elif choix == "2":
        rechercher_donnees_meteo(donnees_meteo)

    elif choix =="3":
        mettre_a_jour_donnees_meteo(donnees_meteo)

    elif choix == "4":
        print("Aurevoir")
        break
    
    else:
        print("Je n'ai pas compris votre choix!")