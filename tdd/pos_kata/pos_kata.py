"""
Point of Sale (POS) Kata

Implements a simple barcode-based price lookup system with total calculation.
"""

import os

# Get current directory and data file path
MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
PRODUCTS_FILE = os.path.join(MODULE_DIR, "products.txt")


def load_products() -> dict:
    """
    Load product barcodes and prices from a file.
    File format:
        barcode,price
    Example:
        12345,7.25
        23456,12.50
    """
    products = {}
    if not os.path.exists(PRODUCTS_FILE):
        raise FileNotFoundError(f"Products file '{PRODUCTS_FILE}' not found")

    with open(PRODUCTS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 2:
                barcode, price = parts
                products[barcode.strip()] = float(price.strip())
    return products


# Load products once when the module is imported
try:
    PRODUCTS = load_products()
except FileNotFoundError:
    PRODUCTS = {}


def scan(barcode: str) -> str:
    """
    Simulate scanning a barcode and return the result message.

    Rules:
    1. Barcode '12345' -> '$7.25'
    2. Barcode '23456' -> '$12.50'
    3. Barcode not found -> 'Error: barcode not found'
    4. Empty barcode -> 'Error: empty barcode'
    """
    if not barcode:
        return "Error: empty barcode"

    if barcode in PRODUCTS:
        return f"${PRODUCTS[barcode]:.2f}"

    return "Error: barcode not found"


def calculate_total(barcodes: list[str]) -> str:
    """
    Calculate the total price for a list of scanned barcodes.
    """
    total = 0.0
    for barcode in barcodes:
        if barcode in PRODUCTS:
            total += PRODUCTS[barcode]
    return f"Total: ${total:.2f}"
