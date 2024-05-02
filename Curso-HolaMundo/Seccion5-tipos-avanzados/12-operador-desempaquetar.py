lista1 = [1, 2, 3, 4]
# print(lista)
# print(*lista)
lista2 = [5, 6]
combinada = [*lista1, *lista2]
print(combinada)

punto1 = {"x": 19}
punto2 ={"y": 16}
nuevopunto = {**punto1, **punto2} #para usar el desempaquetamiento con diccionarios se usa doble asterisco
print(nuevopunto)
