#ejercicio calculadora utilizando controles de flujo
print("Bienvenido a la calculadora")
print("Para salir escribe Salir")
print("Las operaciones son suma, multi, div y resta")

num1 = int(input("Ingrese número: "))

op = ""

if num1 == "":
    num1 = int(input("Ingrese número: "))

else:
    while True:
        op = input("Ingrese operacion: ")
        if op.lower() == "salir":
            break
        num2 = int(input("Ingrese siguiente numero: "))
        if op == "suma":
            num1 += num2
        elif op == "multi":
            num1 *= num2
        elif op == "div":
            num1 /= num2
        elif op == "resta":
            num1 -= num2
        else: 
            print("Operacion no encontrada")
        print(f"El resultado es {num1}")