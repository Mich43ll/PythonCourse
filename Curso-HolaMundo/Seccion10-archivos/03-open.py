from io import open

# Escritura
# texto = "Hola mundo!"

# archivo = open("Curso-HolaMundo/Seccion10-archivos/hola-mundo.txt", "w")
# archivo.write(texto)

# archivo.close()

# # Lectura
# archivo = open("Curso-HolaMundo/Seccion10-archivos/hola-mundo.txt", "r")
# texto = archivo.read()
# archivo.close()
# print(texto)

#Lectura como lista
# archivo = open("Curso-HolaMundo/Seccion10-archivos/hola-mundo.txt", "r")
# texto = archivo.readlines()
# archivo.close()
# print(texto)

#With y seek
# with es como un try catch, lo unico que al ejecutarse con with el archivo, 
# automaticamente cierra el archivo al terminar la instruccion 
# Y Seek, sirve para poder indicarle al codigo desde que caracter en mi archivo 
# va a empezar a imprimir
# with open("Curso-HolaMundo/Seccion10-archivos/hola-mundo.txt", "r") as archivo:
#     print(archivo.readlines())
#     archivo.seek(0)
#     for linea in archivo:
#         print(linea)

# Agregar 
# archivo = open("Curso-HolaMundo/Seccion10-archivos/hola-mundo.txt", "a+")
# archivo.write("Chao mundo :(")
# archivo.close()

# lectura y escritura 
with open("Curso-HolaMundo/Seccion10-archivos/hola-mundo.txt", "r+") as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0] = "Chanchito feliz la"
    archivo.writelines(texto)
    # El metodo writelines sirve para poder escribir una lista dentro de nuestro archivos 
    # de esta manera no sera necesaria la iteracion 
