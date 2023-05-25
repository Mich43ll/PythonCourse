class Empleado:
    def __init__(self, nombre,salario, anios):
        self.nombre = nombre
        self.salario =salario
        self.anios = anios

    def salario_neto (self):
        salario = self.salario
        total_porcentaje = 0
        for a in range(self.anios):
            porcentaje = (self.salario*0.05)
            total_porcentaje += porcentaje
        neto = total_porcentaje + salario
        print(f"Nombre: {self.nombre}\nAños de antigüedad: {self.anios}\nSalario actual: {neto}")

empleado1 = Empleado("Mario", 6000,10)
empleado1.salario_neto()