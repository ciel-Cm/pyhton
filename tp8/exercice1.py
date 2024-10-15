# 1. Création d'un dictionnaire vide pour stocker les données géographiques
donnees_geographiques = {}

# 2. Ajout des données géographiques pour trois communes
def initialiser_donnees():
    donnees_geographiques["Paris"] = "75000"
    donnees_geographiques["Marseille"] = "13000"
    donnees_geographiques["Lyon"] = "69000"

# 3. Affichage des données géographiques
def afficher_donnees():
    for commune, code_postal in donnees_geographiques.items():
        print(f"{commune}: {code_postal}")

# 4. Recherche des données géographiques
def rechercher_commune(nom_commune):
    return donnees_geographiques.get(nom_commune, None)

# 5. Fonction pour mettre à jour les données géographiques
def mettre_a_jour_commune(nom_commune, nouveau_code_postal):
    if nom_commune in donnees_geographiques:
        donnees_geographiques[nom_commune] = nouveau_code_postal
        print(f"Les données pour {nom_commune} ont été mises à jour.")
    else:
        print(f"La commune {nom_commune} n'existe pas.")

# Programme principal
def main():
    initialiser_donnees()
    afficher_donnees()
    
    while True:
        nom_commune = input("Entrez le nom de la commune que vous souhaitez rechercher (ou 'quit' pour quitter) : ")
        
        if nom_commune.lower() == 'quit':
            print("Merci d'avoir utilisé le programme.")
            break

        resultat = rechercher_commune(nom_commune)
        
        if resultat:
            print(f"Le code postal de {nom_commune} est {resultat}.")
            choix = input("Souhaitez-vous mettre à jour les données de cette commune ? (oui/non) : ")
            if choix.lower() == 'oui':
                nouveau_code_postal = input("Entrez le nouveau code postal : ")
                mettre_a_jour_commune(nom_commune, nouveau_code_postal)
        else:
            print(f"La commune {nom_commune} n'a pas été trouvée.")

# Exécution du programme
if __name__ == "__main__":
    main()
