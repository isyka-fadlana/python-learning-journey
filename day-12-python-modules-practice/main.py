# Managing flow of the program using modules

from storage import load_products, show_products
from validation import is_valid_price
from pricing import calculate_total, calculate_discount

products = load_products()
show_products(products)
print("\n--- Product Details ---")

for product in products:
    name = product["name"]
    price = product["price"]
    quantity = product["quantity"]

    if not is_valid_price(price):
        print(f"Invalid price for {name}. Skipping this product.")
        continue

    total = calculate_total(price, quantity)
    discount = calculate_discount(total)
    print(
        f"Product: {name}\n"
        f"Price: {price}\n"
        f"Discount: {discount}\n"
    )
