# contexto global
saludo = "Hola" #nunca usar variables globales

def saludar():
    global saludo
    saludo = "Hola mundo"
    
def saludaChanchito():
    saludo = "Hola chanchito"
    print(saludo)

#no podemos llamar variables que estan dentro de otras funciones 

print(saludo)
saludar()

