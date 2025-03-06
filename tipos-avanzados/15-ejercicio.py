from pprint import pprint


def eliminar_blancos(texto: str) -> list:
    # return list(filter(lambda char: char != " ", texto))
    return [char for char in texto if char != " "]


def cuenta_caracteres(lista: list):
    char_dict = {}
    for char in lista:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def ordena(dict: dict):
    """ Devuelve una lista de tuplas a partir de un diccionario"""
    return sorted(
        dict.items(),
        key=lambda key: key[1], reverse=True
    )


def mayores_tuplas(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta


def main():
    # 1. Eliminar los espacios en blanco de un string
    # y devolver una lista con los caracteres restantes con comprension de listas
    cadena = "aaabbbbbssssssddddf"  # Ho la Mun do
    sin_espacios = eliminar_blancos(cadena)

    contar_caracteres = cuenta_caracteres(sin_espacios)

    pprint(contar_caracteres, width=1)

    caracteres_ordenados = ordena(contar_caracteres)

    pprint(caracteres_ordenados)

    pprint(mayores_tuplas(caracteres_ordenados))


if __name__ == "__main__":
    main()
