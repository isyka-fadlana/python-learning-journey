import pytest
from pricing import calculate_total

@pytest.mark.parametrize(
    "price, quantity, expected_total",
    [
        (100.0, 3, 300.0),
        (50.0, 1, 50.0),
        (20.0, 5, 100.0),
        (0.0, 10, 0.0),
        (15.5, 2, 31.0),
    ]
)

def test_calculate_total(price, quantity, expected_total):
    total = calculate_total(price, quantity)
    assert total == expected_total

def test_negative_price():
    with pytest.raises(ValueError):
        calculate_total(-10.0, 5)


def test_negative_quantity():
    with pytest.raises(ValueError):
        calculate_total(100.0, -5)