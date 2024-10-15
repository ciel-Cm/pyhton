choix_utilisateur=(input(f"Choissisez votre mot de passe : "))

tentatives=0

while tentatives<=2:
    verification_mot_de_passe=input("Entrez votre mot de passe : ")
    tentatives+=1
    if choix_utilisateur==verification_mot_de_passe:
        print("Connexion réussie")
        print(f"vous avez réussi à vous connecter apres {tentatives} tentatives")
        break
    else:
        print("connexion échouée")
        print(f"vous avez réussi à vous connecter apres {tentatives} tentatives")


