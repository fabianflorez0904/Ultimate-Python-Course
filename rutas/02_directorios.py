from pathlib import Path

path = Path("rutas")

# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("nuevo-nombre.py")

print(path.iterdir())

archivos = [p for p in path.iterdir() if p.is_file()]

archivos_py = [p for p in path.glob("*.py")]

print(archivos_py)
