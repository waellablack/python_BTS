donnees_geographiques ={"Paris":75000,"Lyon":69000,"Marseille":13000}
donnees_geographiques ={}

def ajouter():
    while True:
        choix = input("Voulez vous ajouter un nouveau élément? o/n: ")
        if choix.lower() =="o":
            ville = input("Saisir la clé: ")
            code = input("Saisir la valeur: ")
            if ville in donnees_geographiques:
                print("Existe déja")
            else:
                donnees_geographiques[ville]=code
        else:
            print("Aurevoir")
            break



def afficher():
    if donnees_geographiques:
        print("Contenu du dictinnaires:")
        for cle, valeur in donnees_geographiques.items():
            print(f"{cle} :{valeur}")
    else:
        print("Aucune donnée enregistrée")

def rechercher():
    
    if donnees_geographiques:

        while True:
            ville = input("Veuillez saisir la ville à rechercher: ")
            if ville not in donnees_geographiques:
                print(f"La ville {ville} n'a pas été trouvé dans le dictionnaire")
            else:
                print(f"Le code posale de {ville} est {donnees_geographiques[ville]}")
                break
    else:
        print("Aucune donnée enregistrée")

def modifier():
    if donnees_geographiques:

        while True:
            ville = input("Veuillez saisir la ville à modifier: ")
            if ville not in donnees_geographiques:
                print(f"La ville {ville} n'a pas été trouvé dans le dictionnaire")
            else:
                code = input("Veuillez saisir le nouveau code: ")
                donnees_geographiques[ville]= code
                print(f"Le code posale de {ville} est {donnees_geographiques[ville]}")
                break
    else:
        print("Aucune donnée enregistrée")
    


while True:
    choix = input("""
Que voulez vous faire?
1: ajouter
2: afficher
3: rechercher
4: mettre à jour
5: quitter

> """)
    
    if choix =="1":
        ajouter()

    elif choix == "2":
        afficher()

    elif choix =="3":
        rechercher()

    elif choix =="4":
        modifier()  

    elif choix == "5":
        print("Aurevoir")
        break
    
    else:
        print("Je n'ai pas compris votre choix!")