# nom_de_domaine="sara.fr"
nom_de_domaine=input("Saisir le nom de domaine: ")
nom=nom_de_domaine.split(".") #pour faire les espaces 

print(nom)
dernier_element = nom[-1] # c'est le dernier element du tableau quand on met l'indice à -1
valide=True #l'utilisation du true et du false 
if len(nom)>1: 
    for element in nom: #pour faire le tour de tous les elements
        print(element)
        if len(dernier_element)<=6 and len(dernier_element)>=2 and element.isalnum():  #if 2 <= len(dernier_element) <= 6 en plus simple
            valide=True
            print("Les conditions  sont  satisfaites")
        else :
            print("Les conditions ne sont pas satisfaites")
            valide = False
            break #pour stoper la condition

else:
    print("Trop court")
    valide=False


if valide == True :
    print("bien")
else:
    print("pas bien")
