from abc import ABC, abstractmethod
class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass

class Usuario(Model):
    def guardar(self):
        print("Guardando en BBDD")

class Sesion(Model):
    def guardar(self):
        print("Guardando en archivo")

def guardar(entiendades):
    for entiendad in entiendades:
        entiendad.guardar()
'''
En el polimorfismo creamos multiples objetos con estructuras similares (en este caso por el metodo guardar)
y luego se lo pasamos a una funcion en la cual esta llama a el o los metodos o propiedades de una misma vez 
de esta manera no tenemos que llamar objeto por objeto
'''

usuario = Usuario()
sesion = Sesion()
guardar([sesion, usuario])