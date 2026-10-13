def calculate_cart_total(products: list) -> float:
    total = 0.0
    for product in products:
        total += product["price"]
    return total
