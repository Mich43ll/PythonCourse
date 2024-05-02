punto = { "x": 25, "y": 50} #cada llave se debe de asignar con un string
print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45
print(punto)
if "lala" in punto:
    print("encontre lala", punto["lala"])

######################## Forma de iteractuar con un diccionario ############################
print(punto.get("lala", 96)) # con el metodo get el programa no enviara error
del punto["x"] #eliminar un valor con su llave del dic
del(punto["y"]) 

print(punto)
punto["x"] = 25

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items(): #nos devuelve una tupla con la llave y el valor del diccionario
    print(valor)

for llave, valor in punto.items(): #desempaquetamos la tupla en dos variables 
    print(llave, valor)

######################## Forma real de usar un diccionario ############################
usuarios = [
    {"id": 1, "nombre": "Chanchito"},
    {"id": 2, "nombre": "Juan"},
    {"id": 3, "nombre": "Pedro"},
    {"id": 4, "nombre": "Juan"},
]

for usuario in usuarios:
    print(usuario["nombre"])