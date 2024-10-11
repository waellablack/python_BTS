import random

def analyser_logs_connexion():
    echec = 0
    nb_tentatives = 0
    while nb_tentatives != 10:
        nb_tentatives = nb_tentatives + 1
        if random.randint(0,100) > 50 :
            print(f"Tentative {nb_tentatives}: Connexion réussie.")
            echec = 0

        else:
            print(f"Tentative {nb_tentatives}: Connexion échouée.")
            echec = echec + 1

        if echec >= 3:
            print("Erreur trois tentatives échouées consécutivement. ")
            break
        
    else:
        print("Aucune alerte toutes les tentatives on était verifier.")

analyser_logs_connexion()
