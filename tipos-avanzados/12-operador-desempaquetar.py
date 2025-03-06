lista = [1, 2, 3, 4]
lista2 = [4, 5, 6]

combinada = [*lista, "Hola", *lista2]
print(combinada)

punto1 = {"x": 19}
punto2 = {"y": 52}

coordenada = {**punto1, **punto2}
print(coordenada)
