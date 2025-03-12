ruta = "archivos/archivo-prueba.txt"

# file = open(ruta, "r")

# content = file.read()

# print(content)

# file.close()


with open(ruta, "r", encoding="utf-8") as file:
    content = file.read()
    print(content)


with open(ruta, "w", encoding="utf-8") as file:
    file.write("Hola Mundo")
