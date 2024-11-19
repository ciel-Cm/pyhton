
def est_longueur_valide(mot_de_passe): 

    if len(mot_de_passe)== 8:
        return True  
    else:
        return False
    

def contient_caractere_special(mot_de_passe):
    special = "@#$%&"
def est_ip_valide(ip):
    etat = True
    mesSegments = ip.split(":" if ":" in ip else "-")
    if len(mesSegments)== 6:
        for segment in mesSegments:
            if not est_longueur_valide():
                etat = False
                break   
            else:
                etat = True
    else:
        etat = False
    return etat

# def Saisir_ip():

#     while True:
#         addrese = input("Saisr Mac: ")

#         if est_ip_valide(addrese) :
#             print(f"Cette Mac est valide : {addrese}")
#             break  
#         else :
#             print(f"Veuillez resaisir une Mac valide")
               
# Saisir_ip()           