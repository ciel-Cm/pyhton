
# 66

def est_segment_valide(segment): 
    if segment.isdigit() and 0<= int(segment)<= 255:
        return True  
    else:
        return False
    

def est_ip_valide(ip):
    etat = True
    mesSegments = ip.split(".")
    if len(mesSegments)== 4:
        for segment in mesSegments:
            if not est_segment_valide(segment):
                etat = False
                break   
            else:
                etat = True
    else:
        etat = False
    return etat




def Saisir_ip():

    while True:
        addrese = input("Saisr ip: ")

        if est_ip_valide(addrese) :
            print(f"Cette Ip est valide : {addrese}")
            break  
        else :
            print(f"Veuillez resaisir une Ip valide")
               
Saisir_ip()            
