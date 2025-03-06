class Ave:

    def __init__(self):
        self.volador = "Volador"

    def vuela(self):
        print("Vuela ave")


class Pato(Ave):

    def __init__(self):
        super().__init__()  # Llama el constructor de la clase padre
        self.nadador = "Nadador"

    def vuela(self):
        super().vuela()  # Llamo un metodo de la clase Padre de Pato -> Ave
        print("Vuela Pato")


vale = Pato()

vale.vuela()

print(vale.nadador, vale.volador)
