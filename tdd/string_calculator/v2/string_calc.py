"""
Script that implements the string calculator exercise from
the tddmanifesto.com
"""


def add_strings(numbers):
    """
    Simple string calculator that takes a string and returns an integer.

    For further info check

    https://tddmanifesto.com/exercises/

    Exercise 2 (updated to requirement 2 - handle unknown number of arguments)
    """
    # If empty just return 0
    if numbers == "":
        return 0

    # Split by comma and sum all numbers
    parts = numbers.split(",")
    total = 0
    for part in parts:
        total += int(part)
    return total
