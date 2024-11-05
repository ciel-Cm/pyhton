addrese = input("Saisr ip: ")
ip = addrese.split(".")
segment = addrese.split(".")



def est_sgement_valide(segment):
    
    valide = True
    
    for segment in ip:
                    if segment.isdigit() and 0<= int(segment)<= 255 and addrese.count(".")==3:
                        valide = True  
                    else:
                        valide = False

                    if valide:
                        print(valide)   
                    else:
                        print(valide)

est_sgement_valide(segment)                  

# def est_ip(ip):
#     valide = True

#     while valide == True:
#             for octet in ip:
#                 if octet.isdigit() and 0<= int(octet)<= 255 and addrese.count(".")==3:
#                     valide = True  
#                 else:
#                     valide = False

            # if valide:
            #     print("Valide")   
            # else:
            #     print("Invalide fin")
                           
# est_ip(ip)