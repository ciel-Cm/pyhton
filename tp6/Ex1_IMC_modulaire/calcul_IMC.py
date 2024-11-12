from saisie_poids import saisir_poids
from saisie_taille import saisir_taille

def calculer_IMC():
    poids = saisir_poids()
    taille = saisir_taille()
    imc = poids/((taille*0.01)**2)
    return imc