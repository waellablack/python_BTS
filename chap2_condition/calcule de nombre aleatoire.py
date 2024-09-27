import random

def generer_nombre():
    nombre1 = random.randint(1, 100)
    nombre2 = random.randint(1, 100)
    print(f"Nombre 1 : {nombre1}")
    print(f"Nombre 2 : {nombre2}")
    return nombre1 + nombre2

def demander_calculer(somme_attendue):
    while True:
        try:
            somme = float(input("Veuillez entrer le résultat du calcul : "))
            
            if somme == somme_attendue:
                print("La somme est correcte")
                return True
            else:
                print("La somme n'est pas correcte")
                return False
        except :
            print("Entrée invalide. Veuillez entrer un nombre.")

def demander_recommencer():

    choix = input("Appuyez sur 1 pour recommencer ou sur 2 pour arrêter : ")
    
    while choix not in ['1', '2']:
        choix = input("Choix invalide. Appuyez sur 1 pour recommencer ou sur 2 pour arrêter : ")

    return choix == '1'


somme_attendue = generer_nombre()
if not demander_calculer(somme_attendue):
    if not demander_recommencer():
        print("A la prochaine.")
            
            

