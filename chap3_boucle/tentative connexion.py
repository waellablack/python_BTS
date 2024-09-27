utilisateur_correct = "admin"
max_tentatives = 3
tentatives = 0

while tentatives < max_tentatives:
    nom_utilisateur = input("Entrez le nom d'utilisateur: ")

    if nom_utilisateur == utilisateur_correct:
        print("Connexion réussie !")
        break
    else:
        tentatives += 1
        print(f"Échec de connexion. Tentatives restantes: {max_tentatives - tentatives}")

if tentatives >= max_tentatives:
    print("Nombre maximum de tentatives atteint. Accès bloqué.")
