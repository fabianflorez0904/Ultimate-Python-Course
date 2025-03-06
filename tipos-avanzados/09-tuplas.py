# Las tuplas no se pueden modificar

numeros = (1, 2, 3) + (4, 5, 6)
print(type(numeros))
print(numeros)

cordenada = tuple([1, 2])
print(type(cordenada))
print(cordenada)

print(type(tuple("Hola")), tuple("Hola"))

menosNumeros = numeros[:4]
print(menosNumeros)

# Desempaquedato de la tupla
primero, segundo, tercero, *otros = numeros

print(primero, segundo, tercero, otros)
