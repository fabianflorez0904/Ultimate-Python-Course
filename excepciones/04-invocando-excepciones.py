def divicion(n=0):
    if n == 0:
        raise ZeroDivisionError("No se puede dividir entre 0")
    return 5/n


try:
    print(divicion())
except ZeroDivisionError as ex:
    print(f"Error: {ex}")
