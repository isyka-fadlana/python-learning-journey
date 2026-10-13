import pytest
from pricing import calculate_cart_total

@pytest.fixture
def sample_products():
    return [
        {"name": "Laptop", "price": 1000.0},
        {"name": "Mouse", "price": 50.0},
    ]



def test_calculate_cart_total(sample_products):
    total = calculate_cart_total(sample_products)
    assert total == 1050.0

def test_remove_product(sample_products):
    sample_products.pop()
    assert len(sample_products) == 1

def test_products_count(sample_products):
    assert len(sample_products) == 2

