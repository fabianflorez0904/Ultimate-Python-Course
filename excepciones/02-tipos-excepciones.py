"""Introcuccion al manejo de las excepciones en Python
    """

try:
    n1 = int(input("Ingrese un número: "))
    n2 = int(input("Ingrese otro número: "))
except Exception as ex:

    print(f"Error: {ex}")
    print(type(ex))
