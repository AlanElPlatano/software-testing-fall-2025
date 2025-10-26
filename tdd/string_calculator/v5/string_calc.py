"""
Script that implements the string calculator exercise from
the tddmanifesto.com
"""


def add_strings(numbers):
    """
    Simple string calculator that takes a string and returns an integer.

    For further info check

    https://tddmanifesto.com/exercises/

    Exercise 3 (up to requirement 5)

    Raises:
        ValueError: If the string ends with a separator (comma or newline)
                   or if wrong delimiter is used when custom delimiter is specified
    """
    # If empty just return 0
    if numbers == "":
        return 0

    # Check for custom delimiter
    delimiter = None
    if numbers.startswith("//"):
        # Find the newline that separates delimiter definition from numbers
        newline_pos = numbers.find("\n")
        if newline_pos == -1:
            raise ValueError(
                "Invalid format: missing newline after delimiter definition"
            )

        # Extract the custom delimiter (everything between "//" and "\n")
        delimiter = numbers[2:newline_pos]
        # Extract the numbers part
        numbers = numbers[newline_pos + 1 :]

        # If custom delimiter is specified, validate that only this delimiter is used
        if delimiter:
            # Check for invalid delimiters (comma and newline should not appear)
            for i, char in enumerate(numbers):
                if char in (",", "\n"):
                    raise ValueError(
                        f"'{delimiter}' expected but '{char}' found at position {i}."
                    )

    # Check if string ends with a separator
    if delimiter:
        if numbers.endswith(delimiter):
            raise ValueError("Input cannot end with a separator")
    else:
        if numbers.endswith(",") or numbers.endswith("\n"):
            raise ValueError("Input cannot end with a separator")

    # Replace separators with commas to normalize
    if delimiter:
        numbers = numbers.replace(delimiter, ",")
    else:
        numbers = numbers.replace("\n", ",")

    # Split by comma and sum all numbers
    parts = numbers.split(",")
    total = 0
    for part in parts:
        total += int(part)
    return total
