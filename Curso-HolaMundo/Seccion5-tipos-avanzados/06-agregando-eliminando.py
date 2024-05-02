mascotas = ["pelusa", "pulga", "Felipe","chanchito","pulga"]

mascotas.insert(1, "Melvin") #con insert agregamos un elemento en el indice que queramos
mascotas.append("Chanchito triste") #con append se agrega un nuevo elemento al final de la lista  

mascotas.remove("pulga") #este elimina el primer elemento del arreglo que coincida 
mascotas.pop(1) #elimina el ultimo elemento de la lista si no le pasamos el indice 
del mascotas[0] #con del eliminamos el indice del elemento que queramos 
mascotas.clear() #limpia toda la lista
print(mascotas)