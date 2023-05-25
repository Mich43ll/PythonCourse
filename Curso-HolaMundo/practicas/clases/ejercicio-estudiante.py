class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


    def calificacion(self, p1, p2, p3):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nCalificacion promedio: {round((p1+p2+p3)/3)}")

nota = []
for i in range(3):
    nota.append(int(input(f"Ingrese la nota del parcial {i+1}: ")))

estudiante1 = Estudiante("Michaell", 22)
estudiante1.calificacion(nota[0], nota[1], nota[2])

