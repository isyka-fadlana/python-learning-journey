import pytest
import json
from storage import load_products
from pricing import calculate_cart_total

def test_load_products_and_calculate_total():
    products = load_products()
    total = calculate_cart_total(products)
    assert total == 1050.0

def test_missing_product_file(monkeypatch, tmp_path):
    missing_file_path = tmp_path / "missing_products.json" # for testing missing file scenario

    monkeypatch.setattr(
        "storage.FILE_PATH",
        missing_file_path
    )
    with pytest.raises(FileNotFoundError):
        load_products()

def test_invalid_json(monkeypatch, tmp_path):
    invalid_file = tmp_path / "invalid_products.json"

    invalid_file.write_text(
        '{"name": "Handphone", "price": }',
        encoding="utf-8"
    )
    
    monkeypatch.setattr(
        "storage.FILE_PATH",
        invalid_file
    )
    with pytest.raises(json.JSONDecodeError):
        load_products()