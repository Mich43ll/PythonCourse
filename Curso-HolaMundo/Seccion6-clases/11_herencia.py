class Animal:
    def comer(self):
        print("comiendo")

class Perro(Animal):#Herencia
    def pasear(self):
        print("paseando")

perro = Perro()
perro.comer()

#Esto es una herencia multinivel
#no aplicarlo mas de 2 veces 
#Esta hereda todos los metodos 
#y atributos que la clase haya heredado
class Chanchito(Perro):
    def programar(self):
        print("programando")

chanchito = Chanchito()
chanchito.pasear()