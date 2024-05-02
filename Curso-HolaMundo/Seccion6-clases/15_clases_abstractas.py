from abc import ABC, abstractmethod

class Model(ABC): #Modelo
    @property #el decorador de property sirve para añadir como propiedad a mi clase 
    @abstractmethod #este decorador sirve para que mi propiedad sea obligatoria 
    def tabla(self):
        pass

    @abstractmethod # tambien funciona para los metodos, lo que te obliga a colocar el 
                    # metodo en todas las clases que hereden de model, arroja error ya que tanto la propiedad
                    # como el método son abstractos (obligatorios)
    def guardar(self): #Metodo de guardar del constructor
        pass

    @classmethod
    def buscar_id(self,_id): #metodo de busqueda por ID
        print(f"Buscando por id {_id} en la tabla {self.tabla}")

class Usuario(Model): #Controlador
    tabla = "Usuario"

    def guardar(self):
        print("Guardando Usuario")

class Estudiante(Model):
    tabla = "Estudiante"
    def guardar(self):
        print("No sé")


usuario = Usuario()
estudiante = Estudiante()
estudiante.guardar()
estudiante.buscar_id(123)
usuario.guardar()
Usuario.buscar_id(123)