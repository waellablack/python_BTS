max_tentatives = 3
mot_de_passe_correct = input("Créez un mot de passe : ")
tentatives = 0
while tentatives < max_tentatives:
    mot_de_passe = input("Entrez votre mot de passe : ")
    
    if mot_de_passe == mot_de_passe_correct:
        print("Connexion réussie.")
        break
    else:
        tentatives += 1
        print(f"Mot de passe incorrect. Tentative {tentatives}/{max_tentatives}.")
        
        if tentatives == max_tentatives:
            print("Nombre maximum de tentatives atteint. Accès refusé.")
