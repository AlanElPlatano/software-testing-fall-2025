"""
string calculator testing script
"""

import unittest

from tdd.string_calculator.v1.string_calc import add_strings as add


class TestStringCalculator(unittest.TestCase):
    """String calculator script - only until requirement 1
    https://tddmanifesto.com/exercises/
    """

    def test_empty_string_returns_zero(self):
        """Test that an empty string returns 0"""
        result = add("")
        self.assertEqual(result, 0)

    def test_single_number_returns_value(self):
        """Test that a single number returns that number"""
        result = add("1")
        self.assertEqual(result, 1)

    def test_single_number_different_value(self):
        """Test single number with different value"""
        result = add("5")
        self.assertEqual(result, 5)

    def test_two_numbers_returns_sum(self):
        """Test that two comma-separated numbers return their sum"""
        result = add("1,2")
        self.assertEqual(result, 3)

    def test_two_numbers_different_values(self):
        """Test two numbers with different values"""
        result = add("4,5")
        self.assertEqual(result, 9)

    def test_two_numbers_with_zero(self):
        """Test two numbers where one is zero"""
        result = add("0,5")
        self.assertEqual(result, 5)

    def test_two_zeros(self):
        """Test two zeros"""
        result = add("0,0")
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
