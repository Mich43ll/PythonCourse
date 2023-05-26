class Caminador:
    def caminar(self):
        print("caminando")

class Volador:#Herencia
    def nadar(self):
        print("nadando")

class Perro(Caminador, Volador):#Herencia multiple
    def programar(self):
        print("programando")

'''
Cuando se usa la herencia multiple 
siempre tatar de hacer uso de clases pequeñas
para no tener que estar reemplazando los metodos 
de otras clases en caso de que sean iguales
'''
chanchito = Perro()
chanchito.nadar()
