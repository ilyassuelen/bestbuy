class Store:
    """Manages all products and handles customer orders."""
    def __init__(self, products):
        """Initialize the store with a list of Product objects."""
        self.products = products


    def add_product(self, product):
        """Adds a product to the store."""
        self.products.append(product)


    def remove_product(self, product):
        """Removes a product from store."""
        self.products.remove(product)


    def get_total_quantity(self) -> int:
        """Returns how many items are in the store in total."""
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total


    def get_all_products(self) -> list:
        """Returns all products in the store that are active."""
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products


    def order(self, shopping_list) -> float:
        """Gets a list of tuples: (Product, quantity).
        Buys the products and returns the total price of the order.
        """
        total_price = 0.0

        for product, quantity in shopping_list:
            # Buy the product
            try:
                total_price += product.buy(quantity)
            except Exception as e:
                print(f"Error purchasing {product.name}: {e}")

        return total_price
