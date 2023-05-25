class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def cadena(self):
        print(f"Mi perro {self.nombre} es de raza {self.raza}")

perro1 = Perro("Max", "Pastor Aleman")
perro1.cadena()