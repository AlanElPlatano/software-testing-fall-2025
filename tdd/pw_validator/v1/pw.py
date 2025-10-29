"""
Script that implements the Password input field validation exercise from
the tddmanifesto.com

"""


def validate_password(password: str) -> dict:
    """
    Validate the given password according to the specified rules.

    Args:
        password (str): The password string to validate.

    Returns:
        dict: A dictionary with 'is_valid' (bool) and 'errors' (list of str).
    """
    errors = []

    # Requirement 1: Minimum length of 8 characters
    if len(password) < 8:
        errors.append("Password must be at least 8 characters")

    is_valid = len(errors) == 0

    return {"is_valid": is_valid, "errors": errors}
