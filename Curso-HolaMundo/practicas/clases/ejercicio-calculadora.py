class Calculadora: 
    def suma(self,a ,b):
        print(f"El resultado de la suma es: {a+b}")
    
    def resta(self,a ,b):
        print(f"El resultado de la resta es: {a-b}")

    def multiplicacion(self,a ,b):
        print(f"El resultado de la multiplicacion es: {a*b}")
    
    def division(self,a ,b):
        print(f"El resultado de la division es: {a/b}")
    
calculo = Calculadora()
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
calculo.suma(numero1, numero2)
calculo.resta(numero1, numero2)
calculo.multiplicacion(numero1, numero2)
calculo.division(numero1, numero2)