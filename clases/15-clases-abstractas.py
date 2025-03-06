
from abc import ABC, abstractmethod

# Clase de modelo no esta disenada para generar isntancias de esta


class Model(ABC):

    # Por la propiedad abstraccta se vuelve inesesario definir construcutor

    # def __init__(self):
    #     if not self.tabla:
    #         print("Error, tienes que definir una tabla")

    @property
    @abstractmethod
    def tabla(self):
        pass

    @abstractmethod
    def guardar(self):
        # print(f"Guardando {self.tabla} en BBDD")
        pass

    @classmethod
    def buscar_por_id(self, _id):
        print(f"buscando por id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"

    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD")


user = Usuario()

user.guardar()
Usuario.buscar_por_id(123)
