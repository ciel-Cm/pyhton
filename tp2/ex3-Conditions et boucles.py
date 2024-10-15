import random
continuer= "o"
essai=0
while continuer== "o":
    essai+=1
    nombre1= random.randint(1,10)
    nombre2= random.randint(1,10)
    if nombre1==nombre2:
       print (f"{nombre1}={nombre2}")
       print ("vous avez gagné!")
       print (f"vous etes à votre : {essai} essai")
       continuer= ""
    else :
        print (f"{nombre1}#{nombre2}")
        print (f"vous etes à votre : {essai} essai")
        continuer=str(input ("taper o pour continuer : ") )