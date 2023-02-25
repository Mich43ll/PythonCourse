"""
Instrucciones de la tarea: 
-En el siguiente ejercicio se solicita calcular el area y el perimetro de un Rectangulo,
para ello deberemos crear los siguientes variables 

alto(int)
ancho(int)

-El usuario debe proporcionar los valores de largo y ancho, 
y despues se debe imprimir el resultado en el siguiente formato

Proporciona el alto:
Proporciona el ancho:
Area <area>
Perimetro: <perimetro>

Las formulas para calcular el area y el perimetro de un rectangulo son:
Area: alto * ancho
Perimetro: (alto+ancho)*2
"""

alto = int(input('Proporciona el alto:'))
ancho = int(input('Proporciona el ancho:'))
print(f'Area: {alto*ancho}')
print(f'Perimetro: {(alto+ancho)*2}')
