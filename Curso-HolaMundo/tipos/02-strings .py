nombre_curso = "Ultimate Python"
descripcion_curso = """
Uitmate python, 
este curso contempla todos los detalles
que necesitas aprender para encontrar 
un trabajo como programador 
"""
print(len(nombre_curso)) #len sirve para contar la cantidad de caracteres que hay en un string
print(nombre_curso[0]) #imprime el caracter del indice indiccado
print(nombre_curso[0:8]) #imprime la longitud del caracter que le ingresamos 0 es de donde comenzara y 8 es la longitud
print(nombre_curso[9:]) #igual que el anterior pero solo le indicamos desde donde comenzara a capturar caracteres
print(nombre_curso[:8]) #viceversa que el anterior
print(nombre_curso[:]) #imprime la cadena completa 