import random
# nombre1= random.uniform(20,40)
# nombre2= random.uniform(20,40)
# nombre3= random.uniform(20,40)
# nombre4= random.uniform(20,40)
# nombre5= random.uniform(20,40)
# # nombre6= random.randint(20,40)
# # nombre7= random.randint(20,40)
# # nombre8= random.randint(20,40)
# # nombre9= random.randint(20,40)
# # nombre10= random.randint(20,40)
# tableau=[nombre1, nombre2, nombre3, nombre4, nombre5]


for element in range(10):
    temperature= random.uniform(20,40)
    
    if temperature>35:
        print(f"Alerte!!La temperature est élgale à {temperature:.2f}°C sur le capteur {element+1}")
    
    else :
        print(f"la temperature mesurée est {temperature:.2f}°C sur le capteur {element+1}")