def division(n=0):
    if n==0:
        raise ZeroDivisionError("No se puede dividir por 0", f"{n}")
    return 5 / n

try:
    division()
except ZeroDivisionError as e:
    print(e)

# EVITAR en lo posible, el abuso de excepciones por el hecho de que esto
# puede ser costoso en cuanto a rendimiento 