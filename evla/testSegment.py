def est_segment_valide(segment):
    
    valide = True
    

    if segment.isdigit() and 0<= int(segment)<= 255 :
        valide = True  
    else:
        valide = False

    return valide


# etat = est_segment_valide("19h")

# print(etat)



def est_ip_valide(ip):
    etat = False
    mes_Segements= ip.split(".")
    # print(mes_Segements)
    for segment in mes_Segements:
        # print(segment)
        if est_segment_valide(segment):
            etat = True
        else:
            etat = False
            break
    return etat


etat =  est_ip_valide("192.168.155.1")
print(etat)
    

    # if segment.isdigit() and 0<= int(segment)<= 255 :
    #     valide = True  
    # else:
    #     valide = False

    # return valide
