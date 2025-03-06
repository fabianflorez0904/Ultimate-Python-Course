def get_product(**datos):
    """Esta funcion sirve de ejemplo para las funciones que utilizan los KWARGS
    Keywords arguments
    """
    print(datos)
    for dato in datos:
        print(dato, datos[dato])


get_product(id="711595", nombre="Fabian", dni=1003579366)
