while True :
    def demander_moyenne():
        while True:
            try:
                moyenne = float(input("Veuillez entrer votre moyenne (entre 0 et 20) : "))
                if 0 <= moyenne <= 20:
                    return moyenne
                else:
                    print("La moyenne doit être un nombre entre 0 et 20.")
            except :
                print("Veuillez entrer un nombre valide.")
                
    def appreciation_eleve(moyenne):
        if moyenne >= 18:
            print("Excellent")
        elif 14 <= moyenne < 18:
            print("Très bien")
        elif 10 <= moyenne < 14:
            print("Assez bien")
        elif 5 <= moyenne < 10:
            print("Insuffisant")
        else:
            print("Catastrophique")


    moyenne = demander_moyenne()
    appreciation_eleve(moyenne)
