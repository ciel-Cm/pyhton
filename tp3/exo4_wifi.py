cle_wifi=input("Entrez votre clés WIFI : ")

if cle_wifi.isalnum() :
    if len(cle_wifi)<=8:
        print("il y a très peu de caractères")
    print("Clef valide")
    elif len(cle_wifi)>=63:
    print ("il y a beaucoup de caractères")
    print("Clef invalide")
else: 
    print("Clef invalide")



