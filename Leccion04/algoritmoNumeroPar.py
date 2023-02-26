#Algoritmo para saber si el numero ingresado por el usuario es par o impar

num = int(input('Escribe un valor numerico:'))

if (num%2 == 0):
    print(f'{num} es un numero par')
else:
    print(f'{num} es un numero impar')