#Override Method
class Ave:
    def __init__(self):
        self.vuela = "volador"
    def vuelta(self):
        print("vuela ave")

class Pato(Ave):
    def __init__(self):
        super().__init__()#ejecutar el constructor de la clase padre
        self.nada = "nadador"
    def vuelta(self):
        super().vuelta()#acceder a todos los metodos de la clase padre
        print("vuela pato")

pato = Pato()
pato.vuelta()
#Al tener ambos metodos el mismo nombre, el de la clase padre se cancela
#y se usa el metodo en la clase hija

print(pato.vuela, pato.nada)