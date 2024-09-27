import random

def generer_nombre():
    while True:
        nombre1 = random.randint(1, 20)
        nombre2 = random.randint(1, 20)
        print(f"les nombres sont : {nombre1},{nombre2}")
        
        if nombre1 == nombre2:
            print("les deux nombres sont egaux.")
        else :
            print("les 2 nombre ne sont pas egaux")
        break

generer_nombre()





