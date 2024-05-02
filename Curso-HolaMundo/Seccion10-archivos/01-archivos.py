from pathlib import Path
from time import ctime

archivo = Path("Curso-HolaMundo/Seccion10-archivos/archivo-prueba.txt")
# archivo.exists()
# archivo.rename()
# archivo.unlink()

print("acceso",ctime(archivo.stat().st_atime))
# st_time se refiere a un timestamp que es la fecha que tiene el archivo con
# con respecto al 01/01/1970, esta es una fecha unix

print("creacion",ctime(archivo.stat().st_ctime))
print("modificacion",ctime(archivo.stat().st_mtime))
