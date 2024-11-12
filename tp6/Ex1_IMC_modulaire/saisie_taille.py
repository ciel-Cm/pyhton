def saisir_taille():
    taille = ""
    while taille == "":
        taille = input("Entrez votre taille en cm: ")
        try:
            taille = float(taille)
        except:
            print("Vous n'avez pas saisi une valeur numérique ")
            taille = ""
        else:
            if taille == 0:
                print("Vous avez saisi zéro")
                taille = ""
            elif taille < 0:
                print("Vous avez saisi une valeur négative")
                taille = ""
            elif taille > 260 or taille < 40:
                print("Valeur hors limite")
                taille = ""
    
    return taille