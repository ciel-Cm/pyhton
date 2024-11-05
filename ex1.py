
addrese = input("Saisr ip: ")
ip = addrese.split(".")
segment = addrese.split(".")

# def saisir_ip():

#     saisie = addrese
#     print(ip)
#     if est_segment_valide(segment):
#           print("adresse ip valide")
#     else:
#           print("adresse ip invalide")


def est_segment_valide(segment):
    
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

# def est_ip_valide(ip):

#     print(ip)
#     if est_segment_valide(segment):
#           print(True)
#     else:
#           print(False)

#     est_ip_valide(ip)     
