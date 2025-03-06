# Composition Concept

class Product:

    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - ${self.price} | Stock: {self.stock}"

    def reduce_stock(self, quantity: int):
        """Reduce stock when a product is purchased.

        Args:
            quantity (int): Quantity of product purchased
        """
        if quantity > 0 and self.stock >= quantity:
            self.stock -= quantity
            print(f"✅ {quantity}x {self.name} sold! New stock: {self.stock}")
        else:
            print(
                f"❌ Not enough stock for {self.name}. Avialable: {self.stock}")


class ShoppingCart:
    def __init__(self):
        self.items = {}  # Dictionary: {Product: quantity}

    def add_to_cart(self, product: Product, quantity: int):
        """Adds a product to the shopping cart.

        Args:
            product (Product): Product to add to the cart
            quantity (int): Quantity of producto to add to the cart
        """
        if quantity > 0 and product.stock >= quantity:
            if product in self.items:
                self.items[product] += quantity
            else:
                self.items[product] = quantity
            print(f"🛒 Added {quantity}x {product.name} to the cart.")

        else:
            print(
                f"⚠ Not enough stock for {product.name}. Available: {product.stock}")

    def remove_from_cart(self, product: Product):
        if product in self.items:
            del self.items[product]
            print(f"❌ Removed {product.name} from the cart.")
        else:
            print(f"⚠ {product.name} is not in the cart.")

    def display_cart(self):
        if not self.items:
            print("🛒 Your cart is empty.")
        else:
            total = 0
            for product, quantity in self.items.items():
                cost = product.price * quantity
                print(f"{quantity}x {product.name} - ${cost}")
                total += cost
            print(f"💰 Total: ${total}")

    def checkout(self):
        if not self.items:
            print("⚠ Your cart is empty. Add items before checkout.")
            return

        total_cost = 0
        for product, quantity in self.items.items():
            product.reduce_stock(quantity)  # Deduct stock
            total_cost = product.price * quantity

        self.items.clear()  # Empty cart after purchase

        print(f"✅ Purchase completed! Total cost: ${total_cost}")


class Store:
    def __init__(self, name: str):
        """Contructor Method

        Args:
            name (str): Name of the store
        """
        self.name = name
        self.products = []  # list of products

    def add_product(self, product: Product):
        """Adds a new producto to the store.

        Args:
            product (Product): The new product Object
        """
        self.products.append(product)
        print(f"🛒 {product.name} added to {self.name}")

    def remove_product(self, product_name: str):
        """Remove a product from the store by name.

        Args:
            product_name (str): Name of the product that it goint to be removed
        """
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"❌ {product.name} removed from {self.name}")
                return

        print(f"⚠️ Product {product_name} not found.")

    def display_products(self):
        """Display all products availables in the store.
        """
        print(f"\n🛍 Available Products in {self.name}:")
        for product in self.products:
            print(product)

    def sell_product(self, product_name: str, quantity: int):
        """Handles the sale of a product.

        Args:
            product_name (str): Name of a product to sell
            quantity (int): Quantitu of a product to sell
        """
        for product in self.products:
            if product.name == product_name:
                product.reduce_stock(quantity)
                return
        print(f"⚠️ Product {product_name} not found.")

    def create_cart(self):
        return ShoppingCart()


if __name__ == "__main__":

    # Create Store
    my_store = Store("Pancho Market")

    # Create Products
    apple = Product("Apple", 1.5, 50)
    milk = Product("Milk", 2.0, 20)
    bread = Product("Bread", 1.2, 15)

    bad_apple = Product("Bad Apple", 1.5, 50)

    my_store.add_product(apple)
    my_store.add_product(milk)
    my_store.add_product(bread)
    my_store.add_product(bad_apple)

    my_store.remove_product("Bad Apple")

    my_store.display_products()

    cart = my_store.create_cart()

    cart.add_to_cart(apple, 5)
    cart.add_to_cart(milk, 2)
    cart.add_to_cart(bread, 10)
    cart.add_to_cart(bread, 10)
    cart.add_to_cart(apple, 2)

    cart.display_cart()

    cart.remove_from_cart(milk)

    cart.display_cart()
    cart.checkout()

    my_store.display_products()
