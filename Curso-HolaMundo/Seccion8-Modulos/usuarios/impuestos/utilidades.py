if __name__ != "__main__":
    from ..gestion.crud import guardar #import relativo
    from usuarios.gestion.crud import guardar #import absoluto
    def pagar_impuestos():
        print("Pagando impuestos")
        guardar()

if __name__ == "__main__":
    print("Tarea de mantenimiento")
    
#esto es un import condicionado