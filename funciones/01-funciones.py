def hola():
    print("Hola Mundo")
    print("Papasito lindo")


def print_msg(mensaje, nombres="Anonimo"):
    print(
        f"El mensaje enviado por el usuario {nombres} es \n-->{mensaje.upper()}")


if __name__ == "__main__":
    hola()
    print("Hola Mundooooooo")

    print_msg("Buenos dias solecito")
    print_msg(nombres="Florez", mensaje="Mensajitooo")
