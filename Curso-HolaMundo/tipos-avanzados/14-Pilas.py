pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)
iltimoElemento = pila.pop()
pila.pop()
pila.pop()
print(iltimoElemento)

if not pila:
    print('La pila está vacía')