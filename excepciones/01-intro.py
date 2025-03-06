"""Introcuccion al manejo de las excepciones en Python
    """

try:
    n1 = int(input("Ingrese un número: "))
    n2 = int(input("Ingrese otro número: "))
except:
    print("Error: Ingrese un número válido.")
