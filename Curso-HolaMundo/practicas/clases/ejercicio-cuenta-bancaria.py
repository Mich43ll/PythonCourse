class CuentaBancaria: 
    def __init__(self, cuenta, saldo):
        self.cuenta = cuenta
        self.saldo = saldo

    def deposito(self, deposito):
        self.saldo += deposito
    
    def retiro(self, retiro):
        if self.saldo <= 0:
            print("La cuenta no cuenta con fondos")
        elif retiro > self.saldo:
            print("La cuenta no cuenta con los fondos que necesita")
        else:
            self.saldo-= retiro
        
    def obtenerSaldo(self):
        return f"El saldo de la cuenta {self.cuenta} es de: {self.saldo}"
    
cuenta1 = CuentaBancaria("0702", 100)
cuenta1.deposito(300)
cuenta1.retiro(200)
print(cuenta1.obtenerSaldo())

