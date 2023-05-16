# set significa grupo o conjunto
# coleccion de datos que no se puede repetir y que no esta ordenada 

primer = {1,1,2,2,3,4}
segundo = [3,4,5]


segundo = set(segundo) #convierte la lista en un set
print(primer | segundo) #Union: unir ambos sets
print(primer & segundo) #Interseccion: devuelve los elementos que estan en ambos sets
print(primer - segundo) #diferencia: devuelve los elementos que no se encuentran en el segundo set
print(primer ^ segundo) #diferencia simetrica: devuelve todos los datos que no esten duplicados en ambos sets

#con los sets no podemos acceder a sus datos pero si podriamos: 
if 5 in segundo:
    print('5 esta en segundo')