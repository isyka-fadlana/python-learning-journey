price = 1500.0
quantity = 3
discount_percent = 10.0

def calculate_subtotal(price: float, quantity: int) -> float:
    subtotal = price * quantity
    return subtotal


def apply_discount(subtotal: float, discount_percent: float) -> float:
    discount = subtotal * (discount_percent / 100)
    return discount

def calculate_final_price(subtotal: float, calculate_discount: float) -> float:
    discounted_price = subtotal - calculate_discount
    return discounted_price

subtotal = calculate_subtotal(price, quantity)
discount = apply_discount(subtotal, discount_percent)
final_price = calculate_final_price(subtotal, discount)

print(f"Subtotal: {subtotal}")
print(f"Discount: {discount}")
print(f"Final Price: {final_price}")