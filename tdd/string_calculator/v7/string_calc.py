"""
Script that implements the string calculator exercise from
the tddmanifesto.com


Had to split the responsability into smaller functions because
i got an error saying my code had too many branches, specifically:

pylint R0912: Too many branches

So it was either this or disabling the warning

"""

# Necessary for splitting with RE for requirement 7
import re


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

    Returns:
        list: List of error messages (empty if no errors)
    """
    errors = []
    for i, char in enumerate(numbers):
        if char in (",", "\n"):
            errors.append(f"'{delimiter}' expected but '{char}' found at position {i}.")
    return errors


def _validate_no_trailing_separator(numbers, delimiter):
    """
    Check if string ends with a separator.

    Returns:
        list: List of error messages (empty if no errors)
    """
    if delimiter and numbers.endswith(delimiter):
        return ["Input cannot end with a separator"]
    if not delimiter and (numbers.endswith(",") or numbers.endswith("\n")):
        return ["Input cannot end with a separator"]
    return []


def _extract_all_numbers(numbers, delimiter):
    """
    Extract all numbers from the string, handling both correct and incorrect delimiter usage.
    This ensures we catch all negative numbers even when delimiter errors exist.
    """
    numbers_list = []

    # First, normalize the custom delimiter if it exists
    working_str = numbers
    if delimiter:
        # Replace the custom delimiter with comma for parsing
        working_str = working_str.replace(delimiter, ",")

    # Now split by both comma and newline to catch all numbers
    parts = re.split(r"[,\n]", working_str)

    for part in parts:
        if part:  # Only process non-empty parts
            try:
                numbers_list.append(int(part))
            except ValueError:
                # Skip parts that can't be converted (they're delimiter errors)
                pass

    return numbers_list


def _validate_negative_numbers(numbers_list):
    """
    Check for negative numbers in the parsed list.

    Returns:
        list: List of error messages (empty if no errors)
    """
    negatives = [num for num in numbers_list if num < 0]
    if negatives:
        neg_str = ", ".join(str(n) for n in negatives)
        return [f"Negative number(s) not allowed: {neg_str}"]
    return []


def add_strings(numbers):
    """
    Simple string calculator that takes a string and returns an integer.

    For further info check

    https://tddmanifesto.com/exercises/

    Exercise 3 (up to requirement 7)

    Raises:
        ValueError: If any validation errors occur. Multiple errors are
                   combined into a single message separated by newlines.
    """
    if numbers == "":
        return 0

    all_errors = []

    # Check for custom delimiter
    delimiter = None
    if numbers.startswith("//"):
        try:
            delimiter, numbers = _parse_custom_delimiter(numbers)
        except ValueError as e:
            all_errors.append(str(e))
            # If we can't parse the delimiter, we can't proceed with validation
            if all_errors:
                raise ValueError("\n".join(all_errors)) from e

    # Run all validations and collect errors

    # 1. Custom delimiter validation
    if delimiter:
        all_errors.extend(_validate_custom_delimiter_usage(numbers, delimiter))

    # 2. Trailing separator validation
    all_errors.extend(_validate_no_trailing_separator(numbers, delimiter))

    # 3. Negative number validation (extract numbers even with delimiter errors)
    numbers_list = _extract_all_numbers(numbers, delimiter)
    all_errors.extend(_validate_negative_numbers(numbers_list))

    # If there are any errors, raise them all together
    if all_errors:
        raise ValueError("\n".join(all_errors))

    # If no errors, calculate the sum
    if delimiter:
        normalized = numbers.replace(delimiter, ",")
    else:
        normalized = numbers.replace("\n", ",")

    parts = normalized.split(",")
    total = 0
    for part in parts:
        if part:  # Skip empty parts
            total += int(part)

    return total
