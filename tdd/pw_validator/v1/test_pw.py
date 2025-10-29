"""
Password input field validation testing script
"""

import unittest

from tdd.pw_validator.v1.pw import validate_password


class TestPasswordValidator(unittest.TestCase):
    """password validator script up to requirement 1
    https://tddmanifesto.com/exercises/
    """

    def test_valid_password(self):
        """Test a valid password"""
        result = validate_password("StrongPass1")
        self.assertTrue(result["is_valid"])
        self.assertEqual(len(result["errors"]), 0)

    def test_short_password(self):
        """Test a password that is too short"""
        result = validate_password("Short1")
        self.assertFalse(result["is_valid"])
        self.assertIn("Password must be at least 8 characters", result["errors"])
