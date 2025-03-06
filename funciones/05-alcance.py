# Definicion de variable en contexto Global

saludo = "Hola Mamasitas"


def saludar():
    # print(saludo) No llega la variable definida en contexto Global
    global saludo
    print(saludo)
    saludo = "Hola mundo"
    print(saludo)


def saludarChanchito():
    saludo = "Hola Chanchito"
    print(saludo)


saludar()
print(saludo)

# print(saludo)
# saludar()
# saludarChanchito()
