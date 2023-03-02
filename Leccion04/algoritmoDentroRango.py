#Pedir al usuario que ingrese un valor propocionado es mayor o igual a 0 y menor o igual a 5
valor = int(input('Escriba un valor:'))
valorMaximo = 5
valorMinimo = 0
dentroRango = valor >= valorMinimo and valor <= valorMaximo
if(dentroRango):
    print(f'El valor {valor} esta dentro del rango')
else:
    print(f'El valor {valor} no esta dentro del rango')

#Si el padre tiene vacaciones o es dia de descanso entonces podra asistir al juego, de lo contrario no 
vacaciones = False
diaDescanso = False

if not (vacaciones or diaDescanso):
    print('Tiene deberes por hacer')
else:
    print('Puede asistir al juego')