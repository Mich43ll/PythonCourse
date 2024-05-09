import csv
import os
import time

# escribir 
# with open("Curso-HolaMundo/Seccion10-archivos/archivo.csv", "w") as archivo:
#     writer = csv.writer(archivo)
#     writer.writerow(["tweet_id", "user_id", "text"])
#     writer.writerow([1000, 1,"primer tweet"])
#     writer.writerow([1001, 2,"otro tweet"])

#leer 
# with open("Curso-HolaMundo/Seccion10-archivos/archivo.csv") as archivo:
#     reader = csv.reader(archivo)
#     for row in reader:
#         print(row)

# actualizar csv
with open("Curso-HolaMundo/Seccion10-archivos/archivo.csv") as r, open("Curso-HolaMundo/Seccion10-archivos/arcchivo_temp.csv", "w") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for row in reader:
        if len(row) > 1:
            if row[0] == "1000":
                writer.writerow([1000, 1, "texto modificado"])
            else:
                writer.writerow(row)
        else :
            print(f"Fila con menos de 2 elementos encontrada: {row}")
    time.sleep(1)
    os.remove("Curso-HolaMundo/Seccion10-archivos/archivo.csv")
    os.rename("Curso-HolaMundo/Seccion10-archivos/arcchivo_temp.csv", "Curso-HolaMundo/Seccion10-archivos/archivo.csv")


