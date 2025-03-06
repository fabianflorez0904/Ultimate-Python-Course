class Perro:
    patas = 4

    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):
        print("Guau!")

    @classmethod
    def factory(cls):
        return cls("Lupita", 10)


def main():
    mi_perro = Perro("Roki", 14)
    mi_perro.habla()
    Perro.habla()
    perro2 = Perro.factory()
    print(perro2.edad, perro2.nombre)


if __name__ == "__main__":
    main()
