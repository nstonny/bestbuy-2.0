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

