import random

def connexion_mdp():
    echec = 0
    vrai_mdp = "azerty"
    while echec != 3:
        mdp = input("Entrer le mot de passe : ")
        if mdp != vrai_mdp :
            echec = echec + 1
            print("Mot de passe incorrecte. Veulliez reccommencer !")
        else :
            print("Mot de passe correct. Bienvenue !")
            break
    print("Nombre d'essaie d'epasser")
connexion_mdp()