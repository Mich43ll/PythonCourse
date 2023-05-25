class ListaNumeros:
    def __init__(self):
        self.almacenar = []

    def agregar(self, numero):
        self.almacenar.append(int(numero))

    def eliminar(self):
        print(self.almacenar)
        numero = int(input("Ingrese el numero que desea eliminar:"))
        if numero in self.almacenar:
            self.almacenar.remove(numero)
        else:
            print("El numero no se encuentra en la lista")

    def suma(self):
        sumatoria = 0
        print(self.almacenar)
        for n in self.almacenar:
            sumatoria += n
        print(f"La sumatoria de los numeros de la lista es igual a: {sumatoria}")

lista1 = ListaNumeros()
lista1.agregar(1)
lista1.agregar(2)
lista1.agregar(20)
lista1.agregar(10)
lista1.eliminar()
lista1.suma()
