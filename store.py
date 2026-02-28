class Store:

    def __init__(self, products):
        self._products = list(products)

    def add_product(self, product):
        self._products.append(product)

    def remove_product(self, product):
        self._products.remove(product)

    def get_total_quantity(self):
        return sum(product.get_quantity() for product in self._products)

    def get_all_products(self):
        return [product for product in self._products if product.is_active()]

    def order(self, list_of_products_to_buy):
        # validating shopping list first
        for product, quantity in list_of_products_to_buy:
            if product not in self._products:
                raise Exception("Product not available in store")
            if product.is_stock_managed():
                if quantity > product.get_quantity():
                    raise ValueError("Not enough quantity in store")

        total_price = 0
        for product, quantity in list_of_products_to_buy:
            total_price += product.buy(quantity)
        return total_price



