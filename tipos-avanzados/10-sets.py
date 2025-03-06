# Set significa grupo o conjunto


primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5]

segundo = set(segundo)  # {3,4,5}


print(primer | segundo)  # Union de Sets | Union
print(primer & segundo)  # Interseccion de Sets & Interseccion
print(primer - segundo)  # Diferencia de Sets - Diferencia
print(segundo - primer)  # Diferencia de Sets - Diferencia
print(primer ^ segundo)  # Diferencia simetrica de Sets - Diferencia simetrica

if 5 in segundo:
    print("Si esta el 5")
