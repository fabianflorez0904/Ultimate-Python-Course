class Animal:
    def comer(self):
        print("Comiento")

    def pasear(self):
        print("Paseando animal")


class Perro:

    def pasear(self):
        print("Paseando perros")


class Chanchito(Animal, Perro):  # Herencia multiple
    def programar(self):
        print("Programando")


marranito = Chanchito()

marranito.pasear()
