"""
City Search Functionality Module

This module provides a search function to find cities from a database file
based on various search criteria.
"""

import os
from typing import List

# Get the directory where this module is located
MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
# File path for the cities database - now using absolute path
CITIES_FILE = os.path.join(MODULE_DIR, "cities.txt")


def load_cities() -> List[str]:
    """
    Load city names from the cities.txt file.

    Returns:
        A list of city names

    Raises:
        FileNotFoundError: If cities.txt file doesn't exist
    """
    if not os.path.exists(CITIES_FILE):
        raise FileNotFoundError(f"City database file '{CITIES_FILE}' not found")

    with open(CITIES_FILE, "r", encoding="utf-8") as file:
        cities = [line.strip() for line in file if line.strip()]

    return cities


# Load cities when module is imported
try:
    CITIES = load_cities()
except FileNotFoundError:
    # Fallback to empty list if file doesn't exist
    CITIES = []


def search_city(search_text: str) -> List[str]:
    """
    Search for cities matching the given search text.

    Args:
        search_text: The text to search for in city names

    Returns:
        A list of city names that match the search criteria

    Rules:
        1. If search text has fewer than 2 characters, return empty list
        2. If search text has 2+ characters, return cities containing the text
        3. Search is case-insensitive
        4. Search text can match any part of the city name
        5. If search text is "*", return all cities
    """
    # Rule 5: Return all cities if search text is "*"
    if search_text == "*":
        return CITIES.copy()

    # Rule 1: Return empty list if search text is fewer than 2 characters
    if len(search_text) < 2:
        return []

    # Rule 3: Case-insensitive search
    search_lower = search_text.lower()

    # Rule 2 & 4: Find cities that contain the search text
    results = [city for city in CITIES if search_lower in city.lower()]

    return results
