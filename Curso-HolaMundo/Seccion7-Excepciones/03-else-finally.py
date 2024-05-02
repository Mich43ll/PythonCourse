try: 
    n1 = int(input("Ingresa primer numero: "))
except:
    print("Ocurrio un error :(")
    #el bloque Else solo se ejecuta cuando cuando no hay excepciones
else: 
    print("No ocurrio ningun error")
    #el bloque finally se ejecuta siempre no importa que 
finally:
    print("Se ejecuta siempre")