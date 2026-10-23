import logging
from storage import load_products

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

products = load_products()
print(products)
