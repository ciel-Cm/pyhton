from random import*

def controlerDebit ():
    continuer = 0
    iteration = 0
    compter = 0

    while continuer == 0:
        debit = randint(0, 101)
        compter += 1

        if debit > 100:
            print(f"Itération {compter} : Débit réseau {debit} Mbps dépasse le seuil de 100 Mbps.")
            iteration += 1
        else:
            print(f"Itération {compter} : Débit réseau {debit} Mbps est sous contrôle.")
            iteration = 0
    
        if iteration == 3:
            print(f"Alerte le débit à dépassé 3 de fois de suite le seuil de contrôle. La connexion à donc été intérompue.")
            continuer = 1


controlerDebit()