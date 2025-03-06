def gestionar_inventario(productos, accion, item=None):
    if accion == "agregar":
        productos.append(item)  # Completa con el método correcto
    elif accion == "eliminar":
        if item in productos:
            productos.remove(item)  # Completa con el método correcto
        else:
            print(f"El producto '{item}' no está en el inventario.")
    print("Inventario actualizado:", productos)


# Prueba con:
inventario = ["Laptop", "Mouse", "Teclado"]
gestionar_inventario(inventario, "agregar", "Monitor")
gestionar_inventario(inventario, "eliminar", "Mou")
