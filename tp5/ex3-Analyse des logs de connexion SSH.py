import random


def seconnecter(seuil):

    tentative = 0
    for element in range(10):
        connexion = random.uniform(1, 10)
        
        if connexion > seuil:
            print(f"connexion {element + 1}. ssh réussie.")
        else:
            print(f"connexion {element + 1}. ssh échouée.")
            tentative=tentative+1
    if tentative==3:
        print("compte bloque")
    else:
        print("bienvenue")

seuil = 5
seconnecter(seuil)

