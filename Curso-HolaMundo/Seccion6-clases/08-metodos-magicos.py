class Perro:
    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad 

    def __str__(self):
        return f"Clase Perro: {self.nombre}"
    
    def __del__(self):
        print(f"Charro perro :C {self.nombre}")
    
    def habla(self):
        print(f"{self.nombre} dice: Guau!")

perro1 = Perro("Max", 8)
print(perro1.habla())
del perro1