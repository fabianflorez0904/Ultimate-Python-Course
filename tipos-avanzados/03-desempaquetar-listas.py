numeros = list(range(1, 4))
numeros2 = list(range(11))


print(numeros)

# FEO!
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

primero, segundo, tercero = numeros

print(primero, segundo, tercero)

primero, *otros = numeros

print(primero, otros)

primero, segundo, *otros = numeros2

print(primero, segundo, otros)

primero, segundo, *otros = numeros2

print(primero, segundo, otros)

primero, segundo, *otros, penultimo, ultimo = numeros2

print(primero, segundo,  penultimo, ultimo, otros)
