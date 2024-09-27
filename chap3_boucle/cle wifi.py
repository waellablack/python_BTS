cle_wifi = input("Entrez votre clé Wi-Fi WPA ou WPA2 : ")
if 8 <= len(cle_wifi) <= 63:
    if cle_wifi.isalnum():
        print("clé Wi-Fi valide.")
    else:
        print("La clé Wi-Fi n'est pas valide. Elle doit contenir uniquement des lettres et des chiffres.")
else:
    print("La clé Wi-Fi n'est pas valide. Elle doit contenir entre 8 et 63 caractères.")
