def buscar_empleado(empleados: list, empleado_buscado: str = None) -> tuple:
    for empleado in empleados:
        if empleado_buscado in empleado:
            return empleado
    return None


def imprimir_empleados(empleados: list):
    for i, empleado in enumerate(empleados, start=1):
        print(f"{i}. {empleado[0]} - {empleado[1]}")


def main():
    empleados = [
        ("Carlos", "Ingeniero", 5000),
        ("Ana", "Gerente", 7000),
        ("Luis", "Analista", 4500)
    ]
    informacion_empleado = buscar_empleado(empleados, "Carlos")
    if informacion_empleado:
        nombre, cargo, salario = informacion_empleado
        print(
            f"El nombre es {nombre}, cargo {cargo} con un salario de ${salario}")
    else:
        print("Informacion de empleado no obtenida")
    print()
    imprimir_empleados(empleados)


if __name__ == "__main__":
    main()
