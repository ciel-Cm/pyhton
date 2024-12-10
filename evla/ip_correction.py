
def est_segment_valide(segment): 
    etat = None

    numhex = "0123456789ABCDEF"
   
    if len(segment)== 2:
        for caracater in segment:
            if not caracater in  numhex: 
                etat= False  

                break
            else:
                etat=  True
    else:
        etat = False

    return etat



etat = est_segment_valide()
print(etat)


def est_ip_valide(ip):
    etat = True
    mesSegments = ip.split(":" if ":" in ip else "-")
    if len(mesSegments)== 6:
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
        addrese = input("Saisr Mac: ")

        if est_ip_valide(addrese) :
            print(f"Cette Mac est valide : {addrese}")
            break  
        else :
            print(f"Veuillez resaisir une Mac valide")
               
