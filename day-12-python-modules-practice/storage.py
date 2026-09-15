# Load and Show Products from JSON file

import json
from pathlib import Path

file_path = Path(__file__).parent / 'products.json'

def load_products():
    with open(file_path, 'r') as json_file:
        loaded_data = json.load(json_file)
    return loaded_data

def show_products(products):
    for i, product in enumerate(products, start=1):
        return f"{i}. {product['name']} - Price: {product['price']} - Quantity: {product['quantity']}"