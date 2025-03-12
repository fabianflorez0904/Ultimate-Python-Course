from io import open

# Escritura

texto = "Hola mundo!"

archivo = open("archivos/hola-mundo.txt", "w")

archivo.write(texto)

archivo.close()
