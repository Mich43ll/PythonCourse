class Model(): #Modelo
    tabla = False
    def __init__(self): #constructor del modelo
        if not self.tabla and self.tabla == "":
            print("Error, Tienes que definir una tabla")
        

    def guardar(self): #Metodo de guardar del constructor
        print(f"Guardando {self.tabla} en BBDD")

    @classmethod
    def buscar_id(self,_id): #metodo de busqueda por ID
        print(f"Buscando por id {_id} en la tabla {self.tabla}")

class Usuario(Model): #Controlador
    tabla = "Usuario"

usuario = Usuario()
usuario.guardar()
Usuario.buscar_id(123)