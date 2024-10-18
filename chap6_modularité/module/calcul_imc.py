def calculer_imc():
    taille_cm = float(input("Veuillez saisir votre taille en cm : "))
    poids_kg = float(input("Veuillez saisir votre poids en kg : "))
    if taille_cm <= 0 or poids_kg <= 0:
        print("La taille et le poids doivent être des valeurs positives.") 
    else : 
        pass 
    taille_m = taille_cm / 100  
    imc = poids_kg / (taille_m ** 2)  
    return imc
