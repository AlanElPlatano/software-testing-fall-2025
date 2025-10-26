"""
Script that implements the Password input field validation exercise from
the tddmanifesto.com

"""


def validate_password(password: str) -> dict:
    """
    Validate the given password according to the specified rules.
    """
    errors = []

    # Requirement 1: Minimum length of 8 characters
    if len(password) < 8:
        errors.append("Password must be at least 8 characters")

    # Requirement 2: Must contain at least 2 numbers
    digit_count = sum(1 for char in password if char.isdigit())
    if digit_count < 2:
        errors.append("The password must contain at least 2 numbers")

    # Requirement 3: Must contain at least one capital letter
    if not any(char.isupper() for char in password):
        errors.append("password must contain at least one capital letter")

    # NEW Requirement 4: Must contain at least one special character
    if not any(not char.isalnum() for char in password):
        errors.append("password must contain at least one special character")

    is_valid = len(errors) == 0

    return {"is_valid": is_valid, "errors": errors}
