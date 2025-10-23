class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self) -> int:
        """Returns the quantity (int)."""
        return self.quantity


    def set_quantity(self, quantity):
        """Setter function for quantity. If quantity reaches 0, deactivates the product."""
        self.quantity = quantity
        if quantity == 0:
            self.active = False


    def is_active(self) -> bool:
        """Returns True if the product is active, otherwise False."""
        return self.active


    def activate(self):
        """Activates the product."""
        self.active = True


    def deactivate(self):
        """Deactivates the product."""
        self.active = False


    def show(self):
        """Returns a string that represents the product."""
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"


    def buy(self, quantity) -> float:
        """Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        In case of a problem (when? think about it), raises an Exception.
        """
        if not self.active:
            raise Exception(f"Product '{self.name}' is not active and cannot be purchased.")

        if quantity > self.quantity:
            raise Exception(f"Not enough quantity of '{self.name}' in stock. Available: {self.quantity}")

        # Calculate total price
        total_price = self.price * quantity

        # Adjust quantity
        self.quantity -= quantity

        # If there are no more pieces left: deactivate
        if self.quantity == 0:
            self.active = False

        # Return total price
        return total_price