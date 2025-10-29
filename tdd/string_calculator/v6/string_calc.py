"""
Script that implements the string calculator exercise from
the tddmanifesto.com


Had to split the responsability into smaller functions because
i got an error saying my code had too many branches, specifically:

pylint R0912: Too many branches

So it was either this or disabling the warning

"""


def _parse_custom_delimiter(numbers):
    """
    Extract custom delimiter and numbers from the input string.

    Returns:
        tuple: (delimiter, numbers_string)
    """
    newline_pos = numbers.find("\n")
    if newline_pos == -1:
        raise ValueError("Invalid format: missing newline after delimiter definition")

    delimiter = numbers[2:newline_pos]
    numbers_str = numbers[newline_pos + 1 :]
    return delimiter, numbers_str


def _validate_custom_delimiter_usage(numbers, delimiter):
    """
    Validate that only the custom delimiter is used in the numbers string.

    Raises:
        ValueError: If comma or newline found when custom delimiter specified
    """
    for i, char in enumerate(numbers):
        if char in (",", "\n"):
            raise ValueError(
                f"'{delimiter}' expected but '{char}' found at position {i}."
            )


def _validate_no_trailing_separator(numbers, delimiter):
    """
    Check if string ends with a separator.

    Raises:
        ValueError: If the string ends with a separator
    """
    if delimiter:
        ends_with_separator = numbers.endswith(delimiter)
    else:
        ends_with_separator = numbers.endswith(",") or numbers.endswith("\n")

    if ends_with_separator:
        raise ValueError("Input cannot end with a separator")


def _normalize_separators(numbers, delimiter):
    """
    Replace all separators with commas for uniform processing.

    Returns:
        str: Numbers string with normalized separators
    """
    if delimiter:
        return numbers.replace(delimiter, ",")
    return numbers.replace("\n", ",")


def _check_negatives_and_sum(parts):
    """
    Sum the numbers and check for negatives.

    Returns:
        int: Sum of all numbers

    Raises:
        ValueError: If any negative numbers are found
    """
    negatives = []
    total = 0

    for part in parts:
        num = int(part)
        if num < 0:
            negatives.append(num)
        total += num

    if negatives:
        neg_str = ", ".join(str(n) for n in negatives)
        raise ValueError(f"Negative number(s) not allowed: {neg_str}")

    return total


def add_strings(numbers):
    """
    Simple string calculator that takes a string and returns an integer.

    For further info check

    https://tddmanifesto.com/exercises/

    Exercise 3 (up to requirement 6)

    Raises:
        ValueError: If the string ends with a separator (comma or newline),
                   if wrong delimiter is used when custom delimiter is specified,
                   or if negative numbers are provided
    """
    if numbers == "":
        return 0

    # Check for custom delimiter
    delimiter = None
    if numbers.startswith("//"):
        delimiter, numbers = _parse_custom_delimiter(numbers)
        if delimiter:
            _validate_custom_delimiter_usage(numbers, delimiter)

    # Validate no trailing separators
    _validate_no_trailing_separator(numbers, delimiter)

    # Normalize separators and split
    numbers = _normalize_separators(numbers, delimiter)
    parts = numbers.split(",")

    # Sum and check for negatives
    return _check_negatives_and_sum(parts)
