"""
Script that  implements the string calculator exercise from
the tddmanifesto.com
"""


def add_strings(numbers):
    """
    Simple string calculator that takes a string and returns an integer.

    For further info check

    https://tddmanifesto.com/exercises/

    Exercise 2 (just until requirement 1)
    """
    # If empty just return 0
    if numbers == "":
        return 0

    # If just one number
    if "," not in numbers:
        return int(numbers)

    # By this point we assume we have 2 numbers separated by commas
    parts = numbers.split(",")  # So we split them
    return int(parts[0]) + int(parts[1])  # and add them
