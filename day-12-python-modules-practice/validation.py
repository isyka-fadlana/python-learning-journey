# Validation product prices

def is_valid_price(price):
    if isinstance(price, str):
        try:
            price = float(price)
            return price > 0
        except ValueError:
            return False
        
    elif isinstance(price, (int, float)) and price > 0:
        return True