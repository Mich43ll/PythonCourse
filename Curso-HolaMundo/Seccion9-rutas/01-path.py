from pathlib import Path

# Path(r"C:\Archivos de programa\minecraft") #ruta para windows
# Path("/usr/bin") #ruta absoluta linux
# Path("/one/__init__.py") #ruta relativa

path = Path("hola-mundo/mi-archivo.py")
path.is_file()
path.is_dir()
path.exists()

print(
    path.name,
    path.stem,
    path.suffix,
    path.parent,
    path.absolute()
)

p = path.with_name("chanchito.py")
print(p)
p = path.with_suffix(".bat")
print(p)
p = path.with_stem("Feliz")
print(p)