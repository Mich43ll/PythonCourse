import json 
from pathlib import Path

# escribir json 
# productos = [
#     {"id":1, "name":"Si"},
#     {"id":2, "name":"no"},
#     {"id":3, "name":"tal vez"},
# ]

# data = json.dumps(productos)
# Path("Curso-HolaMundo/Seccion10-archivos/productos.json").write_text(data)

#leer json
data = Path("Curso-HolaMundo/Seccion10-archivos/productos.json").read_text(encoding="utf-8")
productos = json.loads(data)
print(productos)

#modificar json
productos[0]["name"]= "Chanchito feliz"
Path("Curso-HolaMundo/Seccion10-archivos/productos.json").write_text(json.dumps(productos))