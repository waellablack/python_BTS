import random

def bande_passante():
    test = 0
    iteration = 0
    while test != 3 :
        debit = random.randint(1,200)
        if debit > 100 :
            iteration = iteration + 1
            print (f"iteration {iteration}: Débit réseau {debit} Mbps dépasse le seuil de 100 Mbps")
            test += 1

        else:
            iteration += 1
            print (f"iteration {iteration}: Débit réseau {debit}")
            test = 0
    print("Erreur le seuil a était dépasser 3 fois consécutivement")
bande_passante()