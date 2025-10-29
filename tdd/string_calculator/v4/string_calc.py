"""
Script that implements the string calculator exercise from
the tddmanifesto.com
"""


def add_strings(numbers):
    """
    Simple string calculator that takes a string and returns an integer.

    For further info check

    https://tddmanifesto.com/exercises/

    Exercise 3 (up to requirement 4)

    Raises:
        ValueError: If the string ends with a separator (comma or newline)
    """
    # If empty just return 0
    if numbers == "":
        return 0

    # Check if string ends with a separator
    if numbers.endswith(",") or numbers.endswith("\n"):
        raise ValueError("Input cannot end with a separator")

    # Replace newlines with commas to normalize separators
    numbers = numbers.replace("\n", ",")

    # Split by comma and sum all numbers
    parts = numbers.split(",")
    total = 0
    for part in parts:
        total += int(part)
    return total
