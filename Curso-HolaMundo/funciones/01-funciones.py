# al declarar el apellido con el valor "Feliz" este se vuelve el valor por defecto para esta variable
# en caso de que no le enviemos un argumento al parametro
def hola(nombre, apellido="Feliz"): #esta es una funcion con un parametro
    print("Hola mundo!!!")
    print(f"Bienvenido {nombre} {apellido}")


hola("Michaell", "Osorio") #cuando llamamos la funcion a este se le llama Argumento
hola("Chanchito")

hola(apellido="Michaell",nombre="Barahona") #al nombrar el argumento, podemos ingresarlo en cualquier orden

