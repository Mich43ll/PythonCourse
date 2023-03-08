animal = "  ChanCHito feliz  "
print(animal.upper())
print(animal.lower())
print(animal.strip().capitalize()) #primera mayuscula y el resto minuscula 
print(animal.title()) #primera letra de cada palabra en mayuscula
print(animal.strip()) #Remueve espacios vacios al comienzo y al final
print(animal.lstrip()) #quita los espacio del principio
print(animal.rstrip()) #quita los espacio del final
print(animal.find("CH")) #devuelve el indice de la letra que indicamos
print(animal.replace("CH", "ch")) #reemplaza el primer argumento por el segundo argumento
print("nCH" in animal) #devuelve true si encuentra los caracteres y false si no lo encuentra
print("nCH" not in animal) #lo mismo que la anterior, pero preguntamos si no se encuentra
