def est_groupe_hex_valide(groupe):
    if len(groupe) != 2:
        print("erreur")
    try:
        valeur = int(groupe, 16)
        return 0 <= valeur <= 255  
    except :
        print("erreur")
def est_mac_valide(adresse_mac):
    if ':' in adresse_mac:
        separateur = ':'
    if '-' in adresse_mac:
        separateur = '-'
    else:
        print("erreur") 
    groupes = adresse_mac.split(separateur)   
    if len(groupes) != 6:
        print("erreur")      
    return all(est_groupe_hex_valide(groupe) for groupe in groupes)
def saisir_mac():
    while True:
        adresse_mac = input("Veuillez saisir une adresse MAC valide: ")   
        if est_mac_valide(adresse_mac):
            print("Adresse MAC valide.")
            break
        else:
            print("Adresse MAC invalide. Veuillez réessayer.")
saisir_mac()
