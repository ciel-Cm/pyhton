
chaine = "4X"
# try:
#     int(chaine, 16)
# except:
#     print("Un caractère n'est pas en hexadecimal")
# else:
#     print(int(chaine, 16))


# etat = True

# for caracter in chaine:
#     if  caracter in chaine:
#         etat = True
#         print(f"le {caracter} est correct")
#     else:
#         print(f"!!!!!le {caracter} n'est pas correct")

#         etat=False

# print(etat)


for caracter in chaine:
    try:
        int(caracter, 16)
    except:
        print(f"le {caracter}: n'est pas correct")

    else:
        print(f"le {caracter}: est correct")

        # print(int(caracter, 16))