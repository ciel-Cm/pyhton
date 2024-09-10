from random import randint
boucle = 0

while boucle == 0:
    nbr1 = randint(1,10)
    nbr2 = randint(1,10)
    resultat = int(input(f"Combien fait {nbr1} + {nbr2}:"" "))

    if (nbr1+nbr2) == resultat:
            print (f"votre resultat est bien {nbr1+nbr2}")
            boucle = 1
    else :
            print (f"Dommage mais le resultat etais {nbr1+nbr2} ")
            boucle = 0