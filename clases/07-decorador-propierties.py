class Perro:

    def __init__(self, nombre):
        self.nombre = nombre

    @property
    def nombre(self):
        print("Pasando por getter")
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        print("Pasandop por setter")
        if nombre.strip():
            self.__nombre = nombre
        return


perro = Perro("Hola")

print(perro.nombre)
