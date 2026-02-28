from abc import ABC, abstractmethod

class Promotion(ABC):
    """
    An abstract class containing abstract methods required by all promotions.
    This class can not be instantiated directly.
    """
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass

class PercentDiscount(Promotion):
    """
    This class is used to apply percentage discount on products.
    It inherits the abstract Promotion class.
    """

    def __init__(self, name, percent):
        """
        :param percent: represents the percentage discount on the product.
        """
        super().__init__(name)
        if percent < 0 or percent > 100:
            raise ValueError("Percent must be between 0 and 100")
        self._percent = percent

    def apply_promotion(self, product, quantity):
        """
        calculates total price after applying percentage discount on product.
        """
        total_without_discount = product.get_price() * quantity
        discount = total_without_discount * (self._percent / 100)
        return total_without_discount - discount

class SecondHalfPrice(Promotion):

    def apply_promotion(self, product, quantity):
        """
        calculates total price with second product discounted at half price.
        """
        product_price = product.get_price()
        pairs = quantity // 2
        remaining_items = quantity % 2

        total_price = 0
        total_price += pairs * (product_price + product_price * 0.5)
        total_price += remaining_items * product_price

        return total_price

class ThirdOneFree(Promotion):

    def apply_promotion(self, product, quantity):
        """
        calculates total price with third product is free.
        """
        product_price = product.get_price()
        groups_of_three = quantity // 3
        remaining_items = quantity % 3

        # for each group of three items, pay for 2
        payable_items = groups_of_three * 2 + remaining_items
        total_price = payable_items * product_price
        return total_price

