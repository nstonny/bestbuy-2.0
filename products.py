class Product:

    def __init__(self, name, price, quantity):
        if name == "":
            raise Exception("Product name cannot be empty")
        if price <= 0:
            raise Exception("Product price can not be zero or negative")
        if quantity < 0:
            raise Exception("Product quantity can not be negative")

        self._name = name
        self._price = price
        self._quantity = quantity
        self._active = True

    def get_quantity(self):
        return self._quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise Exception("Quantity can not be negative")
        self._quantity = quantity
        if self._quantity == 0:
            self.deactivate()

    def is_active(self):
        return self._active

    def activate(self):
        self._active = True

    def deactivate(self):
        self._active = False

    def show(self):
        return f"{self._name}, Price: {self._price}, Quantity: {self._quantity}"

    def buy(self, quantity):
        if not self._active:
            raise Exception("This product is not active")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        total_price = quantity * self._price
        self.set_quantity(self._quantity-quantity)
        return total_price

class NonStockedProduct(Product):

    def __init__(self, name, price):
        # Always initialize with quantity = 0
        super().__init__(name, price, 0)

    def set_quantity(self, quantity):
        if self._quantity != 0:
            raise Exception("Non-stocked products must always have quantity 0")
        super().set_quantity = 0

    def buy(self, quantity):
        if not self._active:
            raise Exception("This product is not active")
        # no quantity tracking needed
        total_price = quantity * self._price
        return total_price

    def show(self):
        return f"{self._name}, Price: {self._price} (Non-stocked product)"

class LimitedProduct(Product):

    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        if maximum <= 0:
            raise ValueError("Maximum quantity must be positive")
        self._maximum = maximum

    def buy(self, quantity):
        if quantity > self._maximum:
            raise Exception(f"Cannot buy more than {self._maximum} quantity per order")
        super().buy(quantity)

    def show(self):
        return (f"{self._name}, Price: {self._price} (Limited product)"
                f"(Limited to {self._maximum} per order)")

