import random


def gestion(seuil):*
    element=0
    tentatives=0
    condition=True
    while condition:

        debit = random.uniform(20, 200)
        element+=1
        if debit > seuil:
            print(f"Itération {element}. Débit réseau {debit:.2f} Mbp a dépassé le seuil {seuil}.")
            tentatives=tentatives+1
        else:
            print(f"Itération {element}. Débit réseau {debit:.2f} Mbp est inférieur au seuil, donc c'est bon.")
        if tentatives==3:
         print("on coupe la conexion")
         condition=False
         break
        else:
            continue
        



seuil = 100
gestion(seuil)
