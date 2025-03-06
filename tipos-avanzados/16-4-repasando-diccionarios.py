def buscar_empleado_id(empleados: list[dict], id_empleado: int) -> dict | None:
    # for empleado in empleados:
    #     if empleado.get("id") == id:
    #         return empleado
    # return None
    return next((emp for emp in empleados if emp["id"] == id_empleado), None)


def imprimir_informacion_empleado(empleado: dict):
    print("Informacion del empleado")
    for clave, valor in empleado.items():
        print(f"{clave}: {valor}")


def procesar_incremento(empleados: list[dict], id_empleado: int, porcentaje_incremento: float):

    empleado = buscar_empleado_id(empleados, id_empleado)

    if not empleado:
        print(
            f"⚠ No se encontró el empleado con el ID proporcionado: {id_empleado}")
        return

    imprimir_informacion_empleado(empleado)

    incremento = empleado["salario"] * (porcentaje_incremento/100)
    empleado["salario"] += incremento

    print(f"\n✅ Incremento del {porcentaje_incremento}% aplicado con éxito!")

    imprimir_informacion_empleado(empleado)


def obtener_entero(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("⚠ Entrada inválida. Ingrese un número válido.")


def obtener_flotante(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("⚠ Entrada inválida. Ingrese un número válido.")


def ordenar_empleados_por_salario(empleados: list[dict]):
    empleados.sort(key=lambda emp: emp["salario"], reverse=True)


def imprimir_lista_empleados(empleados: list[dict]):
    print("Lista de empleados")
    print(f"Total de empleados {len(empleados)}")
    print("id | nombre | edad | cargo | salario")

    for empleado in empleados:
        print(
            f"{empleado["id"]} | {empleado["nombre"]} | {empleado["edad"]} | {empleado["cargo"]} | ${empleado["salario"]}")


def main():
    # Lista de Diccionarios con datos de un empleado

    empleados = [
        {
            "id": 101,
            "nombre": "Carlos Pérez",
            "edad": 30,
            "cargo": "Desarrollador Backend",
            "salario": 4500
        },
        {
            "id": 102,
            "nombre": "Fabian Florez",
            "edad": 24,
            "cargo": "Desarrollador Junior",
            "salario": 1500
        },
        {
            "id": 103,
            "nombre": "Laura Valeria",
            "edad": 25,
            "cargo": "Esposa de Fabian",
            "salario": 9999
        },
    ]

    id_buscado = obtener_entero("Ingrese el ID de empleado solicitado\n>>>")

    empleado = buscar_empleado_id(empleados, id_buscado)

    if empleado:
        imprimir_informacion_empleado(empleado)
    else:
        print("⚠ No hay información del empleado.")
        return

    porcentaje_incremento = obtener_flotante(
        "Ingrese el porcentaje del aumento.\n>>>")

    procesar_incremento(empleados, id_buscado, porcentaje_incremento)

    ordenar_empleados_por_salario(empleados)
    imprimir_lista_empleados(empleados)


if __name__ == "__main__":
    main()
