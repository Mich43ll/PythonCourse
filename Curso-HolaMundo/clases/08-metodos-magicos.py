class Perro:
<<<<<<< HEAD
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
=======
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Clase perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice: Guau!")

perro = Perro("Chanchito", 4)
print(perro)
texto = str(perro)
print(texto)
>>>>>>> 817ee9579f493740d7d118acc860dc195b654a9e
