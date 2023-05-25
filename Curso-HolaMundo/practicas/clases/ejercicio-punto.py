import math


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def distancia(self, other):
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
    
punto1 = Punto(40, 10)
punto2 = Punto(20, -30)

if(punto1 == punto2):
    print("Los puntos son iguales")
else:
    print(Punto.distancia(punto1,punto2))
