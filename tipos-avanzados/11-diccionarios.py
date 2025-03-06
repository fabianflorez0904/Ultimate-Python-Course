# Clave valor

punto = {
    "x": 27,
    "y": 50
}


print(punto["x"])
print(punto["y"])

punto["z"] = 32

print(punto)

if "lala" in punto:
    print(punto["lala"])
else:
    print("no se encuentra", punto)

print(punto.get("x"))

print(punto.get("lala", 0))  # por defecto None

del punto["z"]
print(punto)

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)

print("_"*10)

productos_lista = [
    {"id": 101, "nombre": "Laptop", "precio": 1200},
    {"id": 102, "nombre": "Mouse", "precio": 20},
    {"id": 103, "nombre": "Teclado", "precio": 35},
]

for producto in productos_lista:
    print(f"{producto["nombre"]} ${producto["precio"]}")
