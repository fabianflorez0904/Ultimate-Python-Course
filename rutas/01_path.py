from pathlib import Path

path = Path("hola-mundo/mi-archivo.py")

path.is_file()
path.is_dir()
path.exists()

print(
    path.name,
    path.stem,
    path.suffix,
    path.parent,
    path.absolute(),
    sep="\n\n"
)
