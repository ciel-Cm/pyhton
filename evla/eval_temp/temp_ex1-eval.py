# 1. Création d'un dictionnaire vide pour stocker les ID
reseau = {
    101:{"nom": "Capteur de temperature", "etat":"inactif"},
    102:{"nom": "Capteur de d'humitité", "etat":"actif"},
    # 103:{"nom": "Capteur de pression", "etat":"inactif"} 
}

def ajouter_peripherique(id,nom,etat,reseau):
    while True:
        choix = input("Voulez vous ajouter un nouveau peripherique ? o/n: ")
        if choix.lower() =="o":
            if id in reseau: 
                print("Existe déja")
            else:
                reseau[id]= ("nom",nom,"etat",etat)
                print("Peripherique ajouter ")
        else:
            print("Aurevoir")
            break

ajouter_peripherique(105,"pression","actif",reseau)
print(reseau)

def supprimer_peripherique(id,reseau):
    print(reseau)
    while True:
        choix = input("Voulez vous supprimer un peripherique ? o/n: ")
        if choix.lower() =="o":
            if id in reseau: 
                del reseau[id]
                print("Peripherique supprimer ")

            else:
                print("N'Existe pas ")
                
        else:
            print("Aurevoir")
            break

# supprimer_peripherique(101,reseau)
# print(reseau)
