
# Nombre de la clase en PascalCase o UpperCamelCase
class Perro:
    # Metodos -> funciones que se encuentran dentro de una clase
    def habla(self):
        print("Guau!")


mi_perro = Perro()
print(type(mi_perro))
mi_perro.habla()

print(isinstance(mi_perro, str))
