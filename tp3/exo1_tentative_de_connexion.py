utilisateur_correct = "admin"
max_tentatives = 3
tentatives = 0


# for iter in range(3):
#     saisie=(input("Entrez votre identifiant : "))
#     tentatives += 1
#     if saisie == utilisateur_correct:
#         print(f"Connexion réussi après {tentatives} tentative(s)")
#         break
#     else:
#        print(f"Connexion échouée")




while tentatives<=2:
      saisie=(input("Entrez votre identifiant : "))
      tentatives += 1
      if saisie == utilisateur_correct:
          print(f"Connexion réussi après {tentatives} tentative(s)")
          break
      else:
         print(f"Connexion échouée")

 