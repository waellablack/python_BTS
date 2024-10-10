import random

def jouer():
    # Les choix possibles
    choix_possibles = ["pierre", "feuille", "ciseaux"]
    
    # L'utilisateur fait son choix
    choix_utilisateur = input("Choisissez pierre, feuille ou ciseaux : ").lower()
    
    # Vérifier si le choix de l'utilisateur est valide
    if choix_utilisateur not in choix_possibles:
        print("Choix invalide ! Veuillez réessayer.")
        return
    
    # L'ordinateur fait son choix
    choix_ordinateur = random.choice(choix_possibles)
    
    print(f"\nVous avez choisi : {choix_utilisateur}")
    print(f"L'ordinateur a choisi : {choix_ordinateur}")
    
    # Déterminer le gagnant
    if choix_utilisateur == choix_ordinateur:
        print("Égalité ! 🤝")
    elif (choix_utilisateur == "pierre" and choix_ordinateur == "ciseaux") or \
         (choix_utilisateur == "feuille" and choix_ordinateur == "pierre") or \
         (choix_utilisateur == "ciseaux" and choix_ordinateur == "feuille"):
        print("Vous avez gagné ! 🎉")
    else:
        print("L'ordinateur a gagné ! 😢")

# Lancer le jeu
jouer()
