#las tuplas no se pueden modificar a diferencia de las listas
numeros = (1,2,3) + (4,5,6)
print(numeros)

punto = tuple([1, 2]) #convierte mi lista en una tupla
print(punto)

numero = list(filter(lambda numero: numero>2,numeros ))
print(numero)

primero, segundo = punto
print(primero,segundo)

listaNumeros = list(numeros) #creando una lista en base a la tupla
listaNumeros[1]="mi corazon"
print(listaNumeros)