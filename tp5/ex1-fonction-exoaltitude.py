def verifier(latitude, longitude):
    if -90 <= latitude <= 90 and -180 <= longitude <= 180:
       print("c'est bon")
    else :
        print("c'est pas bon")

verifier(-160,100)