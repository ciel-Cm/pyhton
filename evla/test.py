# address=input(f'entrez une adresse ip entre chaque octet laissez un espace : ')
# segment=address.split(".") # split fait deja un tableau 
# segment=address.replace(" ", ".") 

# nombre=int(input(segment))
# print(segment)

# def est_segment_valide(segment):
#         if len(segment)==3:
#             if segment<255 or segment>0:
#                 print ("votre addresse ip est correcte")
#             else:
#                 print ("l'adresse ip est incorrecte")
#         else :
#                 print("votre addresse ip est invalide")

# exemplemac=int(input(f'entrez une adresse ip entre chaque octet laissez un espace : '))
# #print(len(exemplemac))
# mac=exemplemac.split(".")
# for element in mac:
#     if len(element)<=3 :
#         if element<255 or element>0:
#                 print ("votre addresse ip est correcte")
#         else:
#                 print ("l'adresse ip est incorrecte")
#         invalide=0
#         continue
#     else:
#         invalide=1
#         break

# if invalide == 0:
#       print("adress mac bien")
# else:
#      print("mac pas bien")

addrese = input("Saisr ip: ")
ip = addrese.split(".")

def est_ip(ip):
    valide = False

    for octet in ip:
        if octet.isdigit() and 0<= int(octet)<= 255 and addrese.count(".")==3:
            valide = True  
        else:
            valide = False
            break

    if valide :
        print("Valide")
    else:
        print("Invalide fin")

est_ip(ip)