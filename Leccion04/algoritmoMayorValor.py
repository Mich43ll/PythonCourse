"""
Intrucciones: 
solicitar al usuario dos valores, y determinar cual numero es el mayor
Solicitar al usuario dos valores: 
numero1 (int)
numero2 (int)
Se debe imprimir el mayor de los dos numeros (la salida debe ser identida a la que sigue):
Proporciona el numero 1:
Proporciona  el numero 2:
El numero mayor es: <numeroMayor>
"""

numero1 = int(input('Proporciona el numero 1: '))
numero2 = int(input('Proporciona el numero 2: '))

if numero1 > numero2:
    print(f'El numero mayor es: {numero1}')
else:
    print(f'El numero mayor es: {numero2}')