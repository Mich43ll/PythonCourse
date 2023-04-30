usuarios = [["chanchito",4],["Felipe",1],["Melvin",5]]

#Esta transformacion se le llama map
nombres = [usuario[0] for usuario in usuarios]
#de esta manera podemos tomar una lista y aplicar una transformacion 

#filtrar poor elementos mayores a 2 = filter
#nombres = [usuario for usuario in usuarios if usuario[1]>2]


#nombres = [usuario[0] for usuario in usuarios if usuario[1]>2]

#Asi se utiliza la funcion map
nombres= list(map(lambda usuario: usuario[0], usuarios))

#Este es el uso de filter
menosUsuario = list(filter(lambda usuario:usuario[1] > 2,usuarios))

print(menosUsuario)