# 1. Eliminar los espacios en blanco de un string y devolver una lista con los caracteres restantes
# 2. Contar en un diccionario cuanto se repiten los caracteres de un string 
# 3. Ordenar las llaves de un diccionario por el valor que tienen y devolver una lista que contiene
# tuplas [("a", 3), ("b", 2),("c", 4)]
# 4. De un listado de tuplas, devolver las tuplas que tengan el mayor valor.
# [("a",3), ("b",2), ("c", 4)] -> [("c", 4)]
# 5. crear un mensaje que diga: 
# Los caracteres que mas se repiten con "4" repeticiones son:
# - C
# - D

# estos caracteres deben de ser en mayuscula 

# 6. juntar la solucion de los ejercicios anteriores para encontrar los caracteres que mas se repiten de un string 

def eliminarEspacios(frase):
    lista = []
    for caracter in frase:
        if (caracter != " "):
            lista.append(caracter.upper())
    return lista

def cuentaCaracteres(frase):
    frase = eliminarEspacios(frase)
    diccionario = {}
    for caracter in frase:
        if caracter in diccionario:
            diccionario[caracter] += 1
        else:
            diccionario[caracter] = 1
    return diccionario

def ordenarLlaves(frase):
    frase = cuentaCaracteres(frase)
    fraseOrdenada = sorted(frase.items(), key=lambda x: x[1], reverse=True)
    return fraseOrdenada

def valorMayor(frase):
    frase = ordenarLlaves(frase)
    mayor_valor = max(frase, key=lambda x: x[1])[1]
    tuplas_mayor_valor = [tupla for tupla in frase if tupla[1] == mayor_valor]
    return tuplas_mayor_valor

def mensaje(frase):
    frase = valorMayor(frase)
    valor = 0
    for tupla in frase:
        llave, valor = tupla

    print(f"Los caracteres que mas se repiten con {valor} repeticiones son:")
    for espace in frase:
        print(espace[0])




mensaje("El pequeño negrito")
