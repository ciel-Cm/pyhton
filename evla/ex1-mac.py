
def est_segment_valide(segment): 

    numhex = 1234567890
    carhex = "ABCDEF"
    if len(segment)== 2:
        for test in segment:
            if test in carhex or numhex: 
                return True  
            else:
                return False
    else:
        return False

etat = est_segment_valide("AR")
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
               
