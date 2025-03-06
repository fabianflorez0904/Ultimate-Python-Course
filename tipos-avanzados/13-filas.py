# Filas con caracteristicas FIFO
# First In First Out

from collections import deque

fila = deque([1, 2])
fila.append(3)
fila.append(4)
fila.append(5)

print(fila)

while fila:
    print(fila)
    fila.popleft()
print(fila)
