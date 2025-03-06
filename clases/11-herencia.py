class Animal:
    def comer(self):
        print("Comiento")


class Perro(Animal):  # Herencia de Animal

    def pasear(self):
        print("Paseando")


class Chanchito(Perro):  # Herencia multi-nivel de perro a la vez de animal
    def programar(self):
        print("Programando")


marranito = Chanchito()

marranito.comer()
marranito.pasear()
