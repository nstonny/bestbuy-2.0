import pytest
from products import Product

def test_create_normal_product():
    """checks if product can be created given all the required arguments"""
    product = Product("MacBook Air M2", price = 1450, quantity = 100)
    assert product._name == "MacBook Air M2"
    assert product._price == 1450
    assert product._quantity == 100
    assert product._active == True

def test_create_product_with_invalid_details():
    """checks if exception is raised when product name is not given"""
    with pytest.raises(Exception):
        Product("", price = 1450, quantity = 100)

    """checks if exception is raised when price of product is negative"""
    with pytest.raises(Exception):
        Product("MacBook Air M2", price = -10, quantity = 100)

def test_product_becomes_inactive_when_quantity_is_zero():
    """checks if product becomes inactive when it's quantity becomes zero"""
    product = Product("MacBook Air M2", price = 1450, quantity = 5)
    product.buy(5)
    assert product._quantity == 0
    assert product._active == False

def test_product_purchase_modifies_quantity_and_returns_total_price():
    """checks if product purchase reduces quantity and returns total purchase price"""
    product = Product("MacBook Air M2", price = 1000, quantity = 10)
    total_price = product.buy(5)

    assert product._quantity == 5
    assert total_price == 5000

def test_buying_more_than_available_raises_exception():
    """checks if user wants to buy more than available quantity"""
    product = Product("MacBook Air M2", price = 1450, quantity = 3)
    with pytest.raises(Exception):
        product.buy(5)







