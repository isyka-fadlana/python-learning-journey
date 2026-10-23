import json
import logging
from pathlib import Path

FILE_PATH = Path(__file__).parent / "products.json"

def load_products():
    logging.info("Loading products...")
    
    try:
        with open(FILE_PATH, "r") as file:
            products = json.load(file)

        logging.info("Products loaded successfully.")
        return products
    
    except (FileNotFoundError, json.JSONDecodeError):
        logging.exception("Failed to load products.")
        raise
    