import random
nombre1= random.randint(1,100)
nombre2= random.randint (1,100)
somme=nombre1 + nombre2 #pour avoir le resultat ici je fais pas += 
print("la somme est:",somme)#pour vaoir mon resultat direct 
print (f"calculez la somme des deux nombres : {nombre1} + {nombre2}")
somme_saisie = int(input(f"Sasir la somme des deux nombres : {nombre1} + {nombre2} :"))# ne pas oublier le f avant input et dire que le resultat est un entier
if somme_saisie==somme:
   print ("bravo")
else : 
   print ("c'est faux réésseyez")

