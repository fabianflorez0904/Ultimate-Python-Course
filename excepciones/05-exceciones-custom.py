class MiError(Exception):
    "Esta Class es para manejar errores personalizados"

    def __init__(self, valor, codigo):
        self.valor = valor
        self.codigo = codigo

    def __str__(self):
        return f"Error: {self.valor} codigo: {self.codigo}"


def divicion(n=0):
    if n == 0:
        raise MiError("No se puede dividir entre 0", 404)
    return 5/n


try:
    print(divicion())
except MiError as ex:
    print(f"Error: {ex}")
