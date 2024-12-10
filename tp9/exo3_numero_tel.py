import re

phone_numbers = "+33 6 12 34 56 78, 0123456789, +33 (0)1 23 45 67 89, invalid_number"

# Définition de l'expression régulière pour valider les numéros de téléphone français
phone_pattern = re.compile(r'\+33[-\s(]*\d{1}[-\s)]*\d{2}[-\s)]*\d{2}[-\s)]*\d{2}[-\s)]*\d{2}')

# Recherche de toutes les occurrences dans la chaîne phone_numbers
valid_phone_numbers = phone_pattern.findall(phone_numbers)

# Affichage des numéros de téléphone français valides
print("Numéros de téléphone français valides :")
for phone_number in valid_phone_numbers:
    print(phone_number)
