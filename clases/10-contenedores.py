class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre} - Precio: ${self.precio}"


class Categoria:
    productos = []

    def __init__(self, nombre, productos: list[Producto]):
        self.nombres = nombre
        self.productos = productos

    def agregar(self, product: Producto):
        self.productos.append(product)

    def imprimir(self):
        for producto in self.productos:
            print(producto)


balon = Producto("Balon", 25)

bicicleta = Producto("Bicicleta", 300)

casco = Producto("Casco", 30)

deportes = Categoria("Deportes", [balon, bicicleta])

deportes.agregar(casco)

deportes.imprimir()
