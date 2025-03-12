from pathlib import Path
from time import ctime

archivo = Path('archivos/archivo-prueba.txt')

# archivo.exists()
# archivo.rename()
# archivo.unlink()
# archivo.stat()


print("Accesso", ctime(archivo.stat().st_atime))  # TimeStamp fecha Unix
print("creacion", ctime(archivo.stat().st_ctime))  # TimeStamp fecha Unix
print("modificacion", ctime(archivo.stat().st_mtime))  # TimeStamp fecha Unix
