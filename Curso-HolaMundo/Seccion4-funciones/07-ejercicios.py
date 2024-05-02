'''# Programa para saber si una palabra es palindromo o no'''

def es_palindromo(texto):
    # convertimos todo el texto ingresado a minusculas
    low = texto.lower()
    # creo una lista en donde se va agregar cada letra de la palabra o frase
    contador = []
    # con este for ingreso cada letra del texto a la lista
    for _ in low:
        if _ != " ":  # me aseguro que no agregue los espacios en blanco
            contador.extend(_)  # funcion para agregar elementos a un arreglo
    cantidad = len(contador)  # tomo el tamaño del arreglo
    # lo agrego una variable y le resto uno para que haga bien el recorrido del while
    i = cantidad - 1

    # creo una lista donde se ingresara todo al reves
    reverso = []
    while i >= 0:
        # agrego cada letra del arreglo anterior
        reverso.extend(contador[i])
        # le resto uno para que el arreglo vaya recorriendose al reves
        i -= 1

    # aqui verifico que ambos arreglos sean iguales
    # si devuelve True es palindromo sino no lo Fes
    if (contador == reverso):
        return True
    else:
        return False


print("Abba", es_palindromo("Abba"))
print("Reconocer", es_palindromo("Reconocer"))
print("Amo la paloma", es_palindromo("Amo la paloma"))
print("Hola Mundo", es_palindromo("Hola mundo"))
