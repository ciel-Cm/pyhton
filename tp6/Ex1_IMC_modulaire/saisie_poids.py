def saisir_poids():
    poids = ""
    while poids == "":
        poids = input("Entrez votre poids en kg: ")
        try:
            poids = int(poids)
        except:
            print("Vous n'avez pas saisi une valeur numérique ")
            poids = ""
        else:
            if poids == 0:
                print("Vous avez saisi zéro")
                poids = ""
            elif poids < 0:
                print("Vous avez saisi une valeur négative")
                poids = ""
            elif poids > 300 or poids < 30:
                print("Valeur hors limite")
                poids = ""
    return poids