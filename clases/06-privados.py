class Perro:

    def __init__(self, nombre: str, edad: int):
        self.__nombre = nombre  # Atributo privado
        self.edad = edad

    def habla(self):
        print(f"{self.__nombre} dice: Guau!")

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    @classmethod
    def factory(cls):
        return cls("Lupita", 10)


def main():
    mi_perro = Perro("Roki", 14)
    mi_perro.habla()
    print(mi_perro.get_nombre())
    mi_perro.set_nombre("Lupita")
    print(mi_perro.get_nombre())

    print(mi_perro.__dict__)
    print(mi_perro._Perro__nombre)


if __name__ == "__main__":
    main()
