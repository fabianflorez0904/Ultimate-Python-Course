# Una Pila caracteristica LIFO
# Last in first Out

pila = []

if not pila:
    print("Pila Vacia")
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)

ultimoEliminado = pila.pop()
print(ultimoEliminado, pila)
