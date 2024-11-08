import caracter

mot_de_passe =""
faux = []
caracter_speciale = "@ # $ % &"
def est_longueur_valide(mot_de_passe) :
    if len(mot_de_passe) < 8 :
        print("recommencer")
    else :
        return False 

def contient_caracter_special(mot_de_passe) :
    for i in mot_de_passe:
        if caracter_speciale in mot_de_passe : 
            print("caractere trouver")
        else : 
            return False
        
def conteient_majuscule_et_miniscule() :
    for i in mot_de_passe :
        if mot_de_passe.isdigit():
            return True
        else : 
            return False
        
def contient_chiffre() :


