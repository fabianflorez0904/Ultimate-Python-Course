class Perro:
    patas = 4

    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


def main():
    mi_perro = Perro("Roki", 14)
    mi_perro.habla()
    print(mi_perro.patas)
    print(Perro.patas)


if __name__ == "__main__":
    main()
