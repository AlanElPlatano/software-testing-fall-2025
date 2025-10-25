"""
FizzBuzz implementation module.

This module contains the fizzbuzz function that returns Fizz, Buzz, or FizzBuzz
based on divisibility rules.
"""


def fizzbuzz(n: int) -> list[str] | None:
    """Return 'Fizz' if n is divisible by 3, 'Buzz' if n is divisible by 5."""
    result = []
    if n % 3 == 0 and n % 5 == 0:
        result.append("FizzBuzz")
    elif n % 3 == 0:
        result.append("Fizz")
    elif n % 5 == 0:
        result.append("Buzz")
    else:
        return None  # Return None explicitly

    return result
