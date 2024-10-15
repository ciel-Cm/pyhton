#address_correcte=address.replace(" ", ".") //pour remplacer 
#print(address_correcte) 
#adresse="123 123 123 123"
#adress=adresse.replace(" ", ",")
#print(adresse)
#txt = "apple#banana#cherry#orange"

#x = txt.replace("#", ",") #la methode .replace pour remplacer 

#print(x)
   #tableau.append()//ajouter des choses dans un tableau 


#address=input(f'entrez une adresse ip entre chaque octet laissez un espace : ')
address="123.123.400.156"
address_correcte=address.split(".") # split fait deja un tableau 
nombre=int(address_correcte)
print(address_correcte)
for element in address_correcte:
    if len(element)==3:
        if nombre<255 or nombre>0:
            print ("votre addresse ip est correcte")
        else:
            print ("l'adresse ip est incorrecte")
    else :
            print("votre addresse ip est invalide")


 

