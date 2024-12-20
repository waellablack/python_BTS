def afficher_dictionnaire(dictionnaire):
    if dictionnaire:
        print("Contenu actuel du dictionnaire :")
        for cle, valeur in dictionnaire.items():
            print(f"{cle} : {valeur}")
    else:
        print("Le dictionnaire est vide.")

def ajouter_element(dictionnaire):
    cle = input("Entrez la clé de l'élément à ajouter : ")
    valeur = input(f"Entrez la valeur associée à {cle} : ")
    dictionnaire[cle] = valeur
    print(f"L'élément {cle} a été ajouté avec la valeur {valeur}.")

def supprimer_element(dictionnaire):
    cle = input("Entrez la clé de l'élément à supprimer : ")
    if cle in dictionnaire:
        del dictionnaire[cle]
        print(f"L'élément {cle} a été supprimé.")
    else:
        print(f"L'élément avec la clé {cle} n'existe pas.")

def menu():
    dictionnaire = {}
    while True:
        print("\nQue souhaitez-vous faire ?")
        print("1 : Ajouter un élément")
        print("2 : Supprimer un élément")
        print("3 : Afficher le dictionnaire")
        print("4 : Quitter")
        
        choix = input("Votre choix : ")

        if choix == "1":
            ajouter_element(dictionnaire)
        elif choix == "2":
            supprimer_element(dictionnaire)
        elif choix == "3":
            afficher_dictionnaire(dictionnaire)
        elif choix == "4":
            print("Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez essayer de nouveau.")

if __name__ == "__main__":
    menu()
