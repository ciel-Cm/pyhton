# 1. Création d'un dictionnaire vide pour stocker les données météorologiques
donnees_meteo = {
    "Paris": {"temperature": 20.0, "humidite": 60},
    "New York": {"temperature": 25.0, "humidite": 70},
    "Tokyo": {"temperature": 28.0, "humidite": 80}
}

# 3. Fonction pour afficher les données météorologiques
def afficher_donnees():
    print("\nDonnées météorologiques :")
    for ville, donnees in donnees_meteo.items():
        temperature = donnees["temperature"]
        humidite = donnees["humidite"]
        print(f"{ville}: Température = {temperature}°C, Humidité = {humidite}%")

# 4. Fonction pour rechercher une ville
def rechercher_ville(ville):
    return donnees_meteo.get(ville, None)

# 5. Fonction pour mettre à jour les données météorologiques
def mettre_a_jour_ville(ville, nouvelle_temperature, nouvelle_humidite):
    if ville in donnees_meteo:
        donnees_meteo[ville] = {"temperature": nouvelle_temperature, "humidite": nouvelle_humidite}
        print(f"Les données pour {ville} ont été mises à jour.")
    else:
        print(f"La ville {ville} n'existe pas dans les données.")

# Programme principal
def main():
    afficher_donnees()
    
    while True:
        ville = input("\nEntrez le nom de la ville pour rechercher les données météo (ou 'quit' pour quitter) : ")
        
        if ville.lower() == 'quit':
            print("Merci d'avoir utilisé le programme.")
            break

        resultat = rechercher_ville(ville)
        
        if resultat:
            temperature = resultat["temperature"]
            humidite = resultat["humidite"]
            print(f"{ville}: Température = {temperature}°C, Humidité = {humidite}%")
            
            choix = input("Souhaitez-vous mettre à jour les données de cette ville ? (oui/non) : ")
            if choix.lower() == 'oui':
                try:
                    nouvelle_temperature = float(input("Entrez la nouvelle température : "))
                    nouvelle_humidite = float(input("Entrez le nouveau niveau d'humidité : "))
                    mettre_a_jour_ville(ville, nouvelle_temperature, nouvelle_humidite)
                except ValueError:
                    print("Erreur : Veuillez entrer des valeurs numériques valides pour la température et l'humidité.")
        else:
            print(f"La ville {ville} n'a pas été trouvée dans les données.")

# Exécution du programme
if __name__ == "__main__":
    main()
