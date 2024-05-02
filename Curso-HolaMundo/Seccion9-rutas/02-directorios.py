from pathlib import Path

path = Path("Seccion9-rutas")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("chanchito-feliz")

archivos = [p for p in path.iterdir() if not p.is_dir()]
print(archivos)
archivos = [p for p in path.glob("01-*.py")]
print(archivos)
archivos = [p for p in path.glob("**/*.py")]
print(archivos)
archivos = [p for p in path.rglob("*.py")]


