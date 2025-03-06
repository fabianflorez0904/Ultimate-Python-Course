buscar = 21


for numero in range(20):
    print(numero, numero * "*")
    if numero == buscar:
        print("numero encontrado en la posicion ", numero)
        break
else:
    print("No se encontro el numero buscado")


for char in "Mamasita linda preciosa":
    print(char)
