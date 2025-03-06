class Perro:
    # Metodo Magico
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Metodo Magico
    def __str__(self):
        return f"Clase Perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice: Guau!")

    def __del__(self):
        print(f"Chao Perrito {self.nombre}")


perro = Perro("Chanchito", 7)
print(perro)

texto = str(perro)

print(texto)

del perro

print(perro)
