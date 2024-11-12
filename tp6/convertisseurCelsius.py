def convertisseur_celsius ():  
    continuer = 0
    while continuer == 0:

        erreur = True
        valeur = int(input("Entrer une valeur à convertir : "))

        while erreur:
            choix = int(input("Taper '1' pour convertir de Celsius en Fahrenheit\nTaper '2' pour convertir de Farhenheit en Celsius : "))

            if choix == 1:
                F = (valeur * (9/5)) + 32
                print(f"\n{valeur} degré celsius fait {F:.2f} degré Farhenheit.")
                erreur = False

            elif choix == 2:
                C = (valeur - 32) * (5/9)
                print(f"\n{valeur} degré Farhenheit fait {C:.2f} degré celsius.")
                erreur = False
            else: 
                erreur = True
        arreter = input("\n\nTaper 'O' pour faire une nouvelle conversion sinon une autre touche aléatoire : ")
        
        if arreter != 'o' and arreter != 'O':
            print("Fin du programme")
            continuer = 1