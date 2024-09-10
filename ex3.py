from random import randint
boucle = 0
essais = 0
while boucle == 0:

    nbr1 = randint(1,5)
    nbr2 = randint(1,5)
    
    essais +=1
    
    print (nbr1)
    print (nbr2)
    
    print (f"compteur essais: {essais}")
  
    if (nbr1 == nbr2):
            print (f"les nombres sont égaux")
            boucle = 1
    elif (nbr1 != nbr2 ):
            print (f"les nombres ne sont pas égaux")
            resultat = int(input("voulez vous rejouer (0) ou quitter (1) : "))
            if(resultat == 0):
                boucle = 0
                
            elif(resultat == 1):
                boucle = 1
                while resultat < 1 or resultat > 2:
                    print ("le valeur ne sont pas bonne: ")
