numeros = [2,4,1,5,7,22,75]

numeros2 =sorted(numeros, reverse=True) #devuelve una nueva lista en vez de modificar la que ya existe 
#numeros.sort(reverse=True) #con reverse los ordena al reves
print(numeros)
print(numeros2)

usuarios = [["chanchito",4],["Felipe",1],["Melvin",5]]

'''La funcion sirve para que nos devuelva un elemento de la lista
para que pueda ser usado en la funcion que se le pasa como argumento
luego llamamos mediante un argumento a nuestra funcion en sort mediante la key'''


def ordena(elemento):
    return elemento[1]

#la funcion lambda es una funcion anonima que nos ayuda a aceeder al segundo elemento de nuestro listado sin necesidad de hacer uso de la funcion anterior
usuarios.sort(key=lambda el:el[1], reverse=True)
print(usuarios)