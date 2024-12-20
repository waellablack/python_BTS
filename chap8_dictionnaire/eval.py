import random

reseaux = {1:{"source":"192.168.0.1","destination":"192.168.0.2","type":"IPV4","etat":"transmise"},
           2:{"source":"192.168.0.3","destination":"192.168.0.4","type":"ARP","etat":"perdue"},
           3:{"source":"192.168.0.5","destination":"192.168.0.6","type":"IPV4","etat":"transmise"}
           }
def ajouter_trame (id, source, destination, type, etat, reseaux):
    while True:
        choix = input("Voulez vous ajouter un nouveau élément? o/n: ")
        if choix.lower() =="o":
            id = random.randint(1,100)
            if id in reseaux : 
                print("L'id est deja utiliser")
            else : 
                pass
            reseaux = ["source"] = "192.168.0." ["destination"] = "192.168.0." ["type"] = "IPV4" ["etat"] = "perdue"



def modifier_etat_trame (id, nouvel_etat, reseaux):
    ajouter_trame(id)
    while True:
        if reseaux :
            trame = input("Veuillez saisir l'id a la trame à modifier: ")
            if trame not in reseaux:
                print(f"La trame {trame} n'a pas été trouvé dans la liste")
            else:
                reseaux["etat"]= "Perdue"
                print(f"La trame : {trame} est {reseaux[trame]}")
                break
        else:
            print("Aucune donnée enregistrée")


def supprimer_trame (reseaux):
    del reseaux[1]



def afficher_trame_par_type (type,reseaux):
    if reseaux:
        print("Contenu du dictionnaires:")
        for i, valeur in reseaux:
            print(f"{i} :{valeur}")
    else:
        print("Aucune donnée enregistrée")


def calculer_statistiques (reseaux):
    nb_actif = sum(1 for etat in reseaux.values() if etat =="transmise")
    print(nb_actif)

