
class Usuario():
    def guardar(self):
        print("Guardando en BBDD")


class Sesion():
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
