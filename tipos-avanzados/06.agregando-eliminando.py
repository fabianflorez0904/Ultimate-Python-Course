mascotas = [
    "Roki",
    "Lupita",
    "Liam",
    "Pandora",
    "Lupita",
    "Lupita",
    "Lupita"
]

mascotas.insert(1, "Reveca")
print(mascotas)

mascotas.append("Tequila")

print(mascotas)

mascotas.remove("Lupita")  # Elimina el primer elemento "Lupita" encontrado

print(mascotas)

mascotas.pop()  # Elimina el ultimo elemento de la lista

print(mascotas)

mascotas.pop(3)

print(mascotas)

del mascotas[3]

print(mascotas)

mascotas.clear()
print(mascotas)
