usuarios = [
    ["Fabian", 4, 123543325],
    ["Laura", 5, 123543575],
    ["Valeria", 1, 123543345],
    ["Florez", 9, 123543875],
    ["Sebastian", 8, 123543123]
]

# for usuario in usuarios:
#     nombres.append(usuario[0])

# print(nombres)

# # nombres =  [expresion for item in items]
# nombres = [(usuario[0], usuario[1]) for usuario in usuarios]

# # Filtrado
# nombres = [(usuario[0], usuario[1]) for usuario in usuarios if usuario[1] >= 8]

nombres = list(map(lambda usuario: (usuario[0], usuario[1]), usuarios))

nombres_filtrados = list(filter(lambda usuario: usuario[1] >= 8, usuarios))
print(nombres_filtrados)

numeros = list(range(101))
numeros = list(filter(lambda x: x % 5 == 0, numeros))
print(numeros)

numeros = list(map(lambda x: x * 1.25, numeros))
print(numeros)
