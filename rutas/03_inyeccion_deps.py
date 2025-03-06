from pathlib import Path

path = Path()

paths = [p for p in path.iterdir() if p.is_dir()]

dependencias = {
    "db": "Base de datos",
    "http": "Servidor web",
    "api": "API",
    "grafql": "Grafql",
}


def load(p):
    paquete = __import__(str(p).replace("/", "."))
    try:
        paquete.init(**dependencias)
    except:
        print("El paquete no tiene funcion Init")


list(map(load, paths))

# for p in esto:
#     print(p)
