def verifier_adresse_ip(adresse):
    if adresse.count('.') != 3:
        return False

    octets = adresse.split('.')

    if len(octets) != 4:
        return False

    for octet in octets:
        if not octet.isdigit():
            return False
        
        valeur = int(octet)
        if valeur < 0 or valeur > 255:
            return False

    return True

def main():
    adresse_ip = input("Entrez une adresse IP : ")
    
    if verifier_adresse_ip(adresse_ip):
        print("L'adresse IP est valide.")
    else:
        print("L'adresse IP est invalide.")

if __name__ == "__main__":
    main()
