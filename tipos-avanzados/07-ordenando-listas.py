numeros = [3, 6, 4, 2, 3, 6, 8, 5, 2, 1]

print(numeros)

numeros.sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)

numeros = [3, 6, 4, 2, 3, 6, 8, 5, 2, 1]
print(numeros)

numeros2 = sorted(numeros)
print(numeros2)

numeros2 = sorted(numeros2, reverse=True)
print(numeros2)

usuarios = [
    [4, "Fabian"],
    [5, "Laura"],
    [1, "Valeria"],
    [9, "Florez"],
    [8, "Sebastian"]
]
usuarios2 = [
    ["Fabian", 4, 123543325],
    ["Laura", 5, 123543575],
    ["Valeria", 1, 123543345],
    ["Florez", 9, 123543875],
    ["Sebastian", 8, 123543123]
]


# def ordena(elemento):
#     return elemento[2]
# usuarios2.sort(key=ordena, reverse=True)


# lambda Parametros: ValorRetorno
usuarios2.sort(key=lambda elemento: elemento[1])

print(usuarios2)
