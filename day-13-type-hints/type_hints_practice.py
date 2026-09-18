def calculate_total(price: float, quantity: int) -> float:
    return price * quantity

result = calculate_total(1500, 3)

print(result)  # Output: 4500.0
print(type(result))  # Output: <class 'float'>