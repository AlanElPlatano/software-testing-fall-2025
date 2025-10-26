"""
Password input field validation testing script
"""

import unittest

from tdd.pw_validator.v5.pw import validate_password


class TestPasswordValidator(unittest.TestCase):
    """password validator script up to requirement 1
    https://tddmanifesto.com/exercises/
    """

    def test_valid_password(self):
        """Test a valid password"""
        result = validate_password(
            "StrongPass12!"
        )  # Updated to include special character
        self.assertTrue(result["is_valid"])
        self.assertEqual(len(result["errors"]), 0)

    def test_short_password(self):
        """Test a password that is too short"""
        result = validate_password("Short1!")
        self.assertFalse(result["is_valid"])
        self.assertIn("Password must be at least 8 characters", result["errors"])

    # Requirement 2
    def test_password_with_no_numbers(self):
        """Test a password with no numbers"""
        result = validate_password("NoNumbers!")
        self.assertFalse(result["is_valid"])
        self.assertIn("The password must contain at least 2 numbers", result["errors"])

    def test_password_with_one_number(self):
        """Test a password with only one number"""
        result = validate_password("OneNumber1!")
        self.assertFalse(result["is_valid"])
        self.assertIn("The password must contain at least 2 numbers", result["errors"])

    def test_password_with_two_numbers(self):
        """Test a password with exactly two numbers"""
        result = validate_password("TwoNumber12!")
        self.assertTrue(result["is_valid"])
        self.assertEqual(len(result["errors"]), 0)

    def test_password_with_more_than_two_numbers(self):
        """Test a password with more than two numbers"""
        result = validate_password("Many123Numbers!")
        self.assertTrue(result["is_valid"])
        self.assertEqual(len(result["errors"]), 0)

    def test_short_password_with_insufficient_numbers(self):
        """Test a password that fails both requirements to this point"""
        result = validate_password("Short!")
        self.assertFalse(result["is_valid"])
        # Should contain multiple error messages
        self.assertIn("Password must be at least 8 characters", result["errors"])
        self.assertIn("The password must contain at least 2 numbers", result["errors"])
        self.assertEqual(len(result["errors"]), 2)

    # Requirement 3
    def test_password_with_multiple_errors_somepassword(self):
        """Test 'somepassword' which should have multiple errors"""
        result = validate_password("somepassword")
        self.assertFalse(result["is_valid"])
        # Should contain errors about numbers, capital, and special character but NOT about length
        self.assertNotIn("Password must be at least 8 characters", result["errors"])
        self.assertIn("The password must contain at least 2 numbers", result["errors"])
        self.assertIn(
            "password must contain at least one capital letter", result["errors"]
        )
        self.assertIn(
            "password must contain at least one special character", result["errors"]
        )
        self.assertEqual(len(result["errors"]), 3)

    def test_password_with_multiple_errors_short_and_no_numbers(self):
        """Test a password that is both short and has no numbers"""
        result = validate_password("short")
        self.assertFalse(result["is_valid"])
        # Should contain all four error messages
        self.assertIn("Password must be at least 8 characters", result["errors"])
        self.assertIn("The password must contain at least 2 numbers", result["errors"])
        self.assertIn(
            "password must contain at least one capital letter", result["errors"]
        )
        self.assertIn(
            "password must contain at least one special character", result["errors"]
        )
        self.assertEqual(len(result["errors"]), 4)

    def test_password_with_multiple_errors_short_and_one_number(self):
        """Test a password that is short and has only one number"""
        result = validate_password("short1")
        self.assertFalse(result["is_valid"])
        # Should contain all four error messages
        self.assertIn("Password must be at least 8 characters", result["errors"])
        self.assertIn("The password must contain at least 2 numbers", result["errors"])
        self.assertIn(
            "password must contain at least one capital letter", result["errors"]
        )
        self.assertIn(
            "password must contain at least one special character", result["errors"]
        )
        self.assertEqual(len(result["errors"]), 4)

    # Requirement 4
    def test_password_with_no_capital_letter(self):
        """Test a password with no capital letter"""
        result = validate_password(
            "nocapital12!"
        )  # Has 2 numbers and special char but no capital
        self.assertFalse(result["is_valid"])
        self.assertIn(
            "password must contain at least one capital letter", result["errors"]
        )

    def test_password_with_one_capital_letter(self):
        """Test a password with exactly one capital letter"""
        result = validate_password(
            "Onecapital12!"
        )  # Has 1 capital, 2 numbers, special char
        self.assertTrue(result["is_valid"])
        self.assertEqual(len(result["errors"]), 0)

    def test_password_with_multiple_capital_letters(self):
        """Test a password with multiple capital letters"""
        result = validate_password(
            "MultipleCAPS12!"
        )  # Has multiple capitals, 2 numbers, special char
        self.assertTrue(result["is_valid"])
        self.assertEqual(len(result["errors"]), 0)

    def test_password_with_no_capital_and_insufficient_numbers(self):
        """Test a password with no capital and insufficient numbers"""
        result = validate_password(
            "nocapital1!"
        )  # No capital, only 1 number, has special char
        self.assertFalse(result["is_valid"])
        # Should contain both error messages
        self.assertIn("The password must contain at least 2 numbers", result["errors"])
        self.assertIn(
            "password must contain at least one capital letter", result["errors"]
        )
        self.assertEqual(len(result["errors"]), 2)

    def test_password_with_no_capital_short_and_insufficient_numbers(self):
        """Test a password that fails all three requirements"""
        result = validate_password(
            "short1"
        )  # No capital, short, only 1 number, no special char
        self.assertFalse(result["is_valid"])
        # Should contain all four error messages
        self.assertIn("Password must be at least 8 characters", result["errors"])
        self.assertIn("The password must contain at least 2 numbers", result["errors"])
        self.assertIn(
            "password must contain at least one capital letter", result["errors"]
        )
        self.assertIn(
            "password must contain at least one special character", result["errors"]
        )
        self.assertEqual(len(result["errors"]), 4)  # Updated from 3 to 4

    # Requirement 5
    def test_password_with_no_special_character(self):
        """Test a password with no special character"""
        result = validate_password(
            "NoSpecial12"
        )  # Has length, 2 numbers, capital but no special char
        self.assertFalse(result["is_valid"])
        self.assertIn(
            "password must contain at least one special character", result["errors"]
        )

    def test_password_with_one_special_character(self):
        """Test a password with exactly one special character"""
        result = validate_password(
            "OneSpecial12!"
        )  # Has all requirements including one special char
        self.assertTrue(result["is_valid"])
        self.assertEqual(len(result["errors"]), 0)

    def test_password_with_multiple_special_characters(self):
        """Test a password with multiple special characters"""
        result = validate_password(
            "Multiple!@#12"
        )  # Has multiple special chars, 2 numbers
        self.assertTrue(result["is_valid"])
        self.assertEqual(len(result["errors"]), 0)

    def test_password_with_only_special_character_error(self):
        """Test a password that only fails the special character requirement"""
        result = validate_password(
            "ValidPass12"
        )  # Meets all requirements except special char
        self.assertFalse(result["is_valid"])
        self.assertEqual(len(result["errors"]), 1)
        self.assertIn(
            "password must contain at least one special character", result["errors"]
        )
