from calcul_IMC import calculer_IMC
def afficher():
    imc = calculer_IMC()
    if imc<18:
        print("Vous êtes trop maigre! Votre IMC = {:.2f}".format(imc))
    elif imc>=18 and imc < 25:
        print("Vous êtes Normal.Votre IMC = {:.2f}".format(imc))
    elif imc>=25 and imc < 30:
        print("Vous êtes en surpoids.Votre IMC = {:.2f}".format(imc))
    elif imc>=30 and imc < 35:
        print("Vous êtes obèse.Votre IMC = {:.2f}".format(imc))
    elif imc>=35 :
        print("Vous êtes très obèse.Votre IMC = {:.2f}".format(imc))