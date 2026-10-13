import json
from pathlib import Path

FILE_PATH = Path(__file__).parent / "products.json"

def load_products():
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        products = json.load(file)
    return products