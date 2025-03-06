def suma(a, b):
    return a+b


def suma_xargs(*numeros):  # El asterizco indica que los argumentos van a ser iterables
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado


print(suma(1, 2))
print(suma_xargs(1, 2, 3, 4, 5))
