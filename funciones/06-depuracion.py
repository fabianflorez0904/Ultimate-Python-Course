def largo(texto):
    longitud = 0
    for _ in texto:  # Se puso _ por que no vamos a usar la variable o el iterador
        longitud += 1
    return longitud


print("Chanchito")

# print(largo("Hola Mamasita"))

l = largo("Hola Mamasita")

print(l)
