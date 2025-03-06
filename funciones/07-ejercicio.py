# def es_palindromo_easy(texto):
#     texto_limpio = texto.lower().replace(" ", "")
#     return texto_limpio == texto_limpio[::-1]
#     # print(texto[::-1])


def texto_reverse(texto: str):
    """
    devuelve el texto dado de manera inversa

    Args:
        texto (str): Cadena de texto a invertir

    Returns:
        str: Texto invertido

    Example:
        >>> texto_reverse("Hola")
        'aloH'
    """
    text_reverse = ""
    for n in range(len(texto), 0, -1):
        text_reverse += texto[n-1]

    return text_reverse


def texto_limpio(texto: str) -> str:
    """
    Convierte todo el texto en minusculas y quita los espacios 

    Args:
        texto (str): Cadena de texto que se quiere limpiar

    Returns:
        str: Texto en minusculas y sin espacios
    """
    return texto.lower().replace(" ", "")


def es_palindromo(texto: str) -> bool:
    """
    Verifica si un texto es palindromo.

    Args:
        texto (str): Texto que se desea comprobar si es palindromo.

    Returns:
        bool: Valor booleano respecto si el texto es palindromo o no.
    """
    return texto_limpio(texto) == texto_reverse(texto_limpio(texto))


if __name__ == "__main__":
    print("Abba", es_palindromo("Abba"))
    print("Reconocer", es_palindromo("Reconocer"))
    print("Amo la paloma", es_palindromo("Amo la paloma"))
    print("Hola Mundo", es_palindromo("hola mundo"))
    print("Somos o no somos", es_palindromo("Somos o no somos"))
    print("A mamá, Roma le aviva el amor a papá, y a papá, Roma le aviva el amor a mamá.", es_palindromo(
        "A mama Roma le aviva el amor a papa y a papa Roma le aviva el amor a mama"))
    print(123454321, es_palindromo("123454321"))
