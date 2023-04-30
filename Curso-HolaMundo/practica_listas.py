# Ejercicio: Ordenar una lista

# Escribe un programa que ordene una lista de números de menor a mayor. Tu programa debe:

# Pedir al usuario que ingrese los números, uno por uno.
# Almacenar los números en una lista.
# Ordenar la lista de menor a mayor.
# Imprimir la lista ordenada.

numeros = []
cantidadNumeros = int(input("Ingrese la cantidad de numeros a ingresar: "))

for i in range(cantidadNumeros):
    numero = int(input(f"Ingrese el #{i+1}: "))
    if(numero%2 != 0 ):
        continue
    else:
        numeros.append(numero)
        numeros.sort()

print(numeros)

