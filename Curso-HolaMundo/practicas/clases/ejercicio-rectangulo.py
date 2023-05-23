class Rectangulo():
    def __init__(self, alto, ancho):
        self.alto = alto 
        self.ancho = ancho

    def area(self):
        return self.ancho * self.alto
    
    def perimetro(self):
        return ((self.ancho*2)+ (self.alto*2))
    
    def __str__(self):
        return f"El area del rectangulo es: {self.area()}\nEl perimetro del rectangulo es: {self.perimetro()}"
    
rec1 = Rectangulo(10,15)
print(rec1)