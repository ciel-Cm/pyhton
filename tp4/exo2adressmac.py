exemplemac="6=:c0:57:b6:ff:ea"
#print(len(exemplemac))
mac=exemplemac.split(":")
for element in mac:
    if len(element)==2 and element.isalnum():
        invalide=0
        continue
    else:
        invalide=1
        break

if invalide == 0:
      print("adress mac bien")
else:
     print("mac pas bien")