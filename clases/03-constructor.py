class Perro:

    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


def main():
    mi_perro = Perro("Roki", 14)
    mi_perro.habla()


if __name__ == "__main__":
    main()
