from abc import ABC, abstractmethod


class Model(ABC):

    @abstractmethod
    def guardar(self):
        pass


class Usuario(Model):
    def guardar(self):
        print("Guardando en BBDD")


class Sesion(Model):
    def guardar(self):
        print("Guardando en archivo")


def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()


user = Usuario()
sesion = Sesion()

# guardar(user)
# guardar(sesion)

guardar([user, sesion])
