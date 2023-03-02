edad = int(input('Introduce tu edad: '))

#veintes = edad >=20 and edad < 30
#treintas = edad >=30 and edad <40

#if (edad >=20 and edad < 30) or (edad >=30 and edad <40):
if(20 <= edad <30 ) or (30 <= edad < 40): #version simplificada del if, evitando el uso del and
    print("Dentro del rango de los 20's y 30's")
    #if(veintes):
    #    print("Dentro de los 20s")
    #elif treintas:
    #   print("Dentro de los 30s")
    #else:("Fuera de rango")
else:
    print("No esta dentro de los (20's) ni (30's)")