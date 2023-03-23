# and, or, not
gas = False
encendido = True
edad = 18
#en una "operacion cortocircuito" si la primera evaluacion del and y or
#devuelve false entonces el resto de la sentencia no se seguir evaluando
#ahorrando recursos de computador
if not gas and encendido and edad > 17:
    print("Puedes avanzar")
