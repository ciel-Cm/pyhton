import re 

#utilisation du try exept else try: tester une condition comme le if, except dans le cas ou ca ne
# respecte pas la condition, else dans le cas ou la condition est verifié comme le do  


#mail=input("quel est votre mail :")
#mail="sara@gmail.com"
#lemail= re.split(r'[.@]', mail, maxsplit=2) #methode pour couper le mail 
#if len(lemail)==3:
    #print("c'est une adresse mail correcte" )
#else: 
    #print("ce n'est pas une adresse mail valide")
#--------------------------------------------------------------------------------------   
#mail=input("quel est votre mail :")
#parties=mail.split('@', 1)

#if len(parties)!=1:
    #print("il faut un seul @ ")
    #print("ce n'est pas une adresse mail correcte" )
    
#else:
       #mailexact= parties[1].split('.', 1)
       #print("Vérifier qu'il y a au moins un point dans la partie domaine")
    #if len(mailexact) != 2:
        #print("Il doit y avoir un point dans le domaine après le @.")
        #print("Ce n'est pas une adresse mail correcte.")
    #else:
        #print("C'est une adresse mail valide.")


mail = input("Quel est votre mail : ")

# Étape 1 : Séparer avec un seul @
parties = mail.split('@', 1)

# Vérifier qu'il y a exactement un seul @
if len(parties) != 2:
    print("Il doit y avoir un seul @.")
    print("Ce n'est pas une adresse mail correcte.")
else:
    # Étape 2 : Vérifier que la partie après le @ contient bien un point
    mailexact = parties[1].split('.', 1)
    
    # Vérifier qu'il y a au moins un point dans la partie domaine
    if len(mailexact) != 2:
        print("Il doit y avoir un point dans le domaine après le @.")
        print("Ce n'est pas une adresse mail correcte.")
    else:
        print("C'est une adresse mail valide.")


    
