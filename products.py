class Product:
    """
    This is the Product class. It contains variables and methods common to
    all types of products that inherit this class.
    """
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
        self._promotion = None

    def get_quantity(self):
        return self._quantity

    def get_price(self):
        return self._price

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

    def is_stock_managed(self):
        return True

    def set_promotion(self, promotion):
        self._promotion = promotion

    def get_promotion(self):
        return self._promotion


    def show(self):
        """
        shows total price including if there is promotion or not.
        """
        promo_name = "None"
        if self._promotion:
            promo_name = self._promotion.get_name()
        return f"{self._name}, Price: {self._price}, Quantity: {self._quantity}, Promotion: {promo_name}"

    def buy(self, quantity):
        """
        validates first, applies promotion calculations, finally returns total price.
        """
        if not self._active:
            raise Exception("This product is not active")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if self._promotion:
            total_price = quantity * self._promotion.apply_promotion(self, quantity)
        else:
            total_price = quantity * self._price
        self.set_quantity(self._quantity-quantity)
        return total_price

class NonStockedProduct(Product):
    """
    This is the NonStockedProduct class. It inherits the Product class.
    """
    def __init__(self, name, price):
        # Always initialize with quantity = 0
        super().__init__(name, price, 0)

    def set_quantity(self, quantity):
        raise Exception("Non-stocked products do not support quantity changes.")

    def is_stock_managed(self):
        """
        checks if product is stock managed, needed to ignore quantity checks when ordering.
        """
        return False

    def buy(self, quantity):
        if not self._active:
            raise Exception("This product is not active")
        # no quantity tracking needed
        total_price = quantity * self._price
        return total_price

    def show(self):
        """
        override method to show the product where quantity needs to be shown as unlimited,
        since quantity for non-stocked products are stored as 0 internally.
        """
        promo_name = "None"
        if self._promotion:
            promo_name = self._promotion.get_name()
        return f"{self._name}, Price: {self._price}, Quantity: Unlimited, Promotion: {promo_name}"

class LimitedProduct(Product):
    """
    This is the LimitedProduct class. It inherits the Product class.
    """

    def __init__(self, name, price, quantity, maximum):
        """
        :param maximum: represents the quantity requested when ordering. only a maximum number of items of this product can be ordered.
        """
        super().__init__(name, price, quantity)
        if maximum <= 0:
            raise ValueError("Maximum quantity must be positive")
        self._maximum = maximum

    def buy(self, quantity):
        if quantity > self._maximum:
            raise ValueError(f"Error while making order! Only {self._maximum} is allowed from this product!")
        super().buy(quantity)

    def show(self):
        """
        shows product details including the maximum quantity that can be ordered.
        """
        promo_name = "None"
        if self._promotion:
            promo_name = self._promotion.get_name()
        return f"{self._name}, Price: {self._price}, Limited to 1 per order!, Promotion: {promo_name}"

