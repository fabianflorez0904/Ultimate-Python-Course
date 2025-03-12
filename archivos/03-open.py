from io import open

# Escritura

texto = "Hola mundo!"

ruta = "archivos/hola-mundo.txt"
archivo = open(ruta, "w")

archivo.write(texto)

archivo.close()

archivo = open(ruta, "r")
texto = archivo.read()
archivo.close()
print(texto)

archivo = open(ruta, "r")
texto = archivo.readlines()
archivo.close()
print(texto)
