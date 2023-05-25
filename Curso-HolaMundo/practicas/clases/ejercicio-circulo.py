import math
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return round(math.pi*(self.radio)**2)
    
    def circunferencia(self):
        return round(2*math.pi*self.radio)
    
radio = float(input("Ingrese el radio del circulo: "))
circulo1 = Circulo(radio)
print(f"El area del circulo es: {circulo1.area()}")
print(f"La circunferencia del circulo es: {circulo1.circunferencia()}")