import random


def seconnecter():
    mdp = "admin"
    tentative = 0
    num = -1
    boucle = 0 
    while(boucle ==0):
        test= input("Veuillez entre votre mot de passe : ") 
        num+=1  

        if mdp == test:
            print(f"Tentative {num + 1}: connexion au systeme réussie.")
            boucle = 1
            break
        else:
            print(f"Tentative {num + 1}: connexion au systeme échouée.")
            tentative=tentative+1
            if tentative==3:
                print("Compte bloquer")
                boucle = 1
                break                

seconnecter()

 