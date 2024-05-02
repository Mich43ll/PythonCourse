from pathlib import Path

archivo = Path("Curso-HolaMundo/Seccion10-archivos/archivo-prueba.txt") # busqueda del archivo
texto = archivo.read_text("utf-8").split("\n")  # se divide todo el texto en un arreglo por cada salto de linea
texto.insert(0, "Hola mundo!") #  insertamos la frase al principio de todo el arreglo
archivo.write_text("\n".join(texto), "utf-8") # se escribe dentro del archivo de texto
############################ CUIDADO: al utilizar write_text se reescribe todo el documento, asi que se usa el join para no
############################ eliminar el texto anterior 