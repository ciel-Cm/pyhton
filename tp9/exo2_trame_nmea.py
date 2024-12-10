import re

# La trame NMEA
nmea_data = "$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47"

# Définition de l'expression régulière pour extraire les informations
pattern = r"\$GPGGA,(\d{6}),(\d{2}\d{2}\.\d+),([NS]),(\d{3}\d{2}\.\d+),([EW]),"

# Recherche dans la chaîne
match = re.search(pattern, nmea_data)

# Vérification et extraction des informations si une correspondance est trouvée
if match:
    time = match.group(1)       # Heure (HHMMSS)
    latitude = match.group(2)   # Latitude
    lat_direction = match.group(3)  # Direction de la latitude (N ou S)
    longitude = match.group(4)  # Longitude
    lon_direction = match.group(5)  # Direction de la longitude (E ou W)

    # Affichage des résultats
    print("Heure (HHMMSS):", time)
    print("Latitude:", latitude, lat_direction)
    print("Longitude:", longitude, lon_direction)
else:
    print("Aucune correspondance trouvée pour la trame NMEA.")
