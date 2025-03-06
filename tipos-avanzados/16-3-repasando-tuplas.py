def calcular_ingresos_generados(ventas: list) -> tuple:
    ingresos = 0
    productos_vendidos = {}
    ventas_ingresos = []

    for producto, cantidad, precio_unitario in ventas:

        ingreso_total = cantidad * precio_unitario

        ingresos += ingreso_total

        ventas_ingresos.append(
            (producto, cantidad, precio_unitario, ingreso_total))

        if producto in productos_vendidos:
            productos_vendidos[producto] += cantidad
        else:
            productos_vendidos[producto] = cantidad
    return ingresos, ventas_ingresos, productos_vendidos


def imprimir_ventas_totales(ventas: list):
    print("\n📊 Detalles de ventas:")
    print("producto, cantidad, precio_unitario, total_vendido")
    for i, (producto, cantidad, precio_unitario, total_vendido) in enumerate(ventas, start=1):
        print(f"{i}. {producto} {cantidad} ${precio_unitario}c/u ${total_vendido}")


def identificar_producto_mas_vendido(productos: dict) -> tuple:
    producto_mas_vendido = max(productos, key=productos.get)
    return producto_mas_vendido, productos[producto_mas_vendido]


def main():
    # ventas = (Producto, Cantidad, Precio_unitario)
    ventas = [
        ("Laptop", 2, 3500),
        ("Mouse", 5, 25),
        ("Teclado", 3, 45),
        ("Monitor", 1, 400),
        ("Laptop", 1, 3500),
        ("Mouse", 2, 25)
    ]

    ingresos, ventas_ingresos, productos_vendidos = calcular_ingresos_generados(
        ventas)
    # Calcular el total de ingresos generadios
    print(f"💰 Total de ingresos: ${ingresos}")
    imprimir_ventas_totales(ventas_ingresos)
    producto_mas_vendido, cantidad = identificar_producto_mas_vendido(
        productos_vendidos)
    print(
        f"\n🏆 Producto más vendido: {producto_mas_vendido} ({cantidad} unidades) 🎉")


if __name__ == "__main__":
    main()
