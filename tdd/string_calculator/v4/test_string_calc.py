"""
string calculator testing script
"""

import unittest

from tdd.string_calculator.v4.string_calc import add_strings as add


class TestStringCalculator(unittest.TestCase):
    """String calculator script up to requirement 4
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

    # Tests for multiple numbers (v2)
    def test_three_numbers(self):
        """Test three comma-separated numbers"""
        result = add("1,2,3")
        self.assertEqual(result, 6)

    def test_four_numbers(self):
        """Test four comma-separated numbers"""
        result = add("1,2,3,4")
        self.assertEqual(result, 10)

    def test_five_numbers(self):
        """Test five comma-separated numbers"""
        result = add("2,3,4,5,6")
        self.assertEqual(result, 20)

    def test_many_numbers_with_zeros(self):
        """Test many numbers including zeros"""
        result = add("0,1,0,2,0,3")
        self.assertEqual(result, 6)

    def test_ten_numbers(self):
        """Test ten comma-separated numbers"""
        result = add("1,2,3,4,5,6,7,8,9,10")
        self.assertEqual(result, 55)

    # Tests for newline separator (v3)
    def test_newline_separator(self):
        """Test numbers separated by newlines"""
        result = add("1\n2\n3")
        self.assertEqual(result, 6)

    def test_mixed_comma_and_newline(self):
        """Test mixed comma and newline separators"""
        result = add("1,2\n3")
        self.assertEqual(result, 6)

    def test_newline_with_multiple_numbers(self):
        """Test newline with multiple numbers"""
        result = add("4\n5\n6")
        self.assertEqual(result, 15)

    def test_mixed_separators_complex(self):
        """Test complex mix of comma and newline separators"""
        result = add("1\n2,3\n4,5")
        self.assertEqual(result, 15)

    # Tests for separator validation (v4)
    def test_trailing_comma_raises_error(self):
        """Test that a trailing comma raises ValueError"""
        with self.assertRaises(ValueError):
            add("1,2,")

    def test_trailing_comma_single_number(self):
        """Test that a trailing comma with single number raises ValueError"""
        with self.assertRaises(ValueError):
            add("1,")

    def test_trailing_newline_raises_error(self):
        """Test that a trailing newline raises ValueError"""
        with self.assertRaises(ValueError):
            add("1\n2\n")

    def test_trailing_newline_single_number(self):
        """Test that a trailing newline with single number raises ValueError"""
        with self.assertRaises(ValueError):
            add("5\n")

    def test_trailing_comma_after_newline(self):
        """Test that a trailing comma after mixed separators raises ValueError"""
        with self.assertRaises(ValueError):
            add("1\n2,3,")

    def test_trailing_newline_after_comma(self):
        """Test that a trailing newline after mixed separators raises ValueError"""
        with self.assertRaises(ValueError):
            add("1,2\n3\n")


if __name__ == "__main__":
    unittest.main()
