class Libro:
    def __init__(self, titulo, autor, anio):
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_anio(self):
        return self.__anio

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_autor(self, autor):
        self.__autor = autor

    def set_anio(self, anio):
        self.__anio = anio


libro1 = Libro("Los juegos del hambre", "nose", "2010")
print(f"Titulo: {libro1.get_titulo()}")
libro1.set_titulo("Ready player one")
print(f"Titulo: {libro1.get_titulo()}")
print(f"Autor: {libro1.get_autor()}")
print(f"Año de publicacion: {libro1.get_anio()}")