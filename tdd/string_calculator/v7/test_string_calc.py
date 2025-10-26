"""
string calculator testing script
"""

import unittest

from tdd.string_calculator.v7.string_calc import add_strings as add


class TestStringCalculator(unittest.TestCase):
    """String calculator script up to requirement 7
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

    # Tests for custom delimiters (v5)
    def test_custom_delimiter_semicolon(self):
        """Test custom delimiter with semicolon"""
        result = add("//;\n1;3")
        self.assertEqual(result, 4)

    def test_custom_delimiter_pipe(self):
        """Test custom delimiter with pipe"""
        result = add("//|\n1|2|3")
        self.assertEqual(result, 6)

    def test_custom_delimiter_multichar(self):
        """Test custom delimiter with multiple characters"""
        result = add("//sep\n2sep5")
        self.assertEqual(result, 7)

    def test_custom_delimiter_with_zeros(self):
        """Test custom delimiter with zeros"""
        result = add("//;\n0;5;0")
        self.assertEqual(result, 5)

    def test_custom_delimiter_single_number(self):
        """Test custom delimiter with single number"""
        result = add("//|\n5")
        self.assertEqual(result, 5)

    def test_custom_delimiter_many_numbers(self):
        """Test custom delimiter with many numbers"""
        result = add("//;\n1;2;3;4;5")
        self.assertEqual(result, 15)

    def test_custom_delimiter_wrong_separator_comma(self):
        """Test that using comma with custom delimiter raises error"""
        with self.assertRaises(ValueError) as context:
            add("//|\n1|2,3")
        self.assertIn(
            "'|' expected but ',' found at position 3", str(context.exception)
        )

    def test_custom_delimiter_wrong_separator_newline(self):
        """Test that using newline with custom delimiter raises error"""
        with self.assertRaises(ValueError) as context:
            add("//;\n1;2\n3")
        self.assertIn("';' expected but", str(context.exception))
        self.assertIn("found at position 3", str(context.exception))

    def test_custom_delimiter_trailing_separator(self):
        """Test that trailing custom delimiter raises error"""
        with self.assertRaises(ValueError):
            add("//;\n1;2;")

    def test_custom_delimiter_asterisk(self):
        """Test custom delimiter with asterisk"""
        result = add("//*\n3*4*5")
        self.assertEqual(result, 12)

    # Tests for negative numbers (v6)
    def test_single_negative_number_raises_error(self):
        """Test that a single negative number raises ValueError"""
        with self.assertRaises(ValueError) as context:
            add("-1")
        self.assertEqual(str(context.exception), "Negative number(s) not allowed: -1")

    def test_negative_with_positive_raises_error(self):
        """Test that negative number with positive raises ValueError"""
        with self.assertRaises(ValueError) as context:
            add("1,-2")
        self.assertEqual(str(context.exception), "Negative number(s) not allowed: -2")

    def test_multiple_negatives_raises_error(self):
        """Test that multiple negative numbers raises ValueError with all negatives listed"""
        with self.assertRaises(ValueError) as context:
            add("2,-4,-9")
        self.assertEqual(
            str(context.exception), "Negative number(s) not allowed: -4, -9"
        )

    def test_negative_with_newline_separator(self):
        """Test negative numbers with newline separator"""
        with self.assertRaises(ValueError) as context:
            add("1\n-2\n3")
        self.assertEqual(str(context.exception), "Negative number(s) not allowed: -2")

    def test_multiple_negatives_mixed_separators(self):
        """Test multiple negatives with mixed separators"""
        with self.assertRaises(ValueError) as context:
            add("1,-2\n-3,4")
        self.assertEqual(
            str(context.exception), "Negative number(s) not allowed: -2, -3"
        )

    def test_negative_with_custom_delimiter(self):
        """Test negative number with custom delimiter"""
        with self.assertRaises(ValueError) as context:
            add("//;\n1;-2;3")
        self.assertEqual(str(context.exception), "Negative number(s) not allowed: -2")

    def test_multiple_negatives_custom_delimiter(self):
        """Test multiple negatives with custom delimiter"""
        with self.assertRaises(ValueError) as context:
            add("//|\n-1|2|-3|-4")
        self.assertEqual(
            str(context.exception), "Negative number(s) not allowed: -1, -3, -4"
        )

    def test_all_negatives(self):
        """Test all negative numbers"""
        with self.assertRaises(ValueError) as context:
            add("-1,-2,-3")
        self.assertEqual(
            str(context.exception), "Negative number(s) not allowed: -1, -2, -3"
        )

    # Tests for multiple errors (v7) god this part was hard
    def test_multiple_errors_negative_and_wrong_delimiter(self):
        """Test that multiple errors are returned together separated by newlines"""
        with self.assertRaises(ValueError) as context:
            add("//|\n1|2,-3")
        expected = "'|' expected but ',' found at position 3.\nNegative number(s) not allowed: -3"
        self.assertEqual(str(context.exception), expected)

    def test_multiple_errors_wrong_delimiter_multiple_times(self):
        """Test multiple wrong delimiter errors"""
        with self.assertRaises(ValueError) as context:
            add("//;\n1,2;3\n4")
        error_msg = str(context.exception)
        self.assertIn("';' expected but ',' found at position 1", error_msg)
        self.assertIn("';' expected but", error_msg)
        self.assertIn("found at position 5", error_msg)

    def test_multiple_errors_negatives_and_trailing_separator(self):
        """Test negative numbers with trailing separator"""
        with self.assertRaises(ValueError) as context:
            add("1,-2,")
        error_msg = str(context.exception)
        self.assertIn("Negative number(s) not allowed: -2", error_msg)
        self.assertIn("Input cannot end with a separator", error_msg)

    def test_multiple_errors_all_three_types(self):
        """Test all three types of errors together"""
        with self.assertRaises(ValueError) as context:
            add("//|\n1|-2,")
        error_msg = str(context.exception)
        self.assertIn("'|' expected but ',' found", error_msg)
        self.assertIn("Negative number(s) not allowed: -2", error_msg)

    def test_multiple_wrong_delimiters_with_negatives(self):
        """Test multiple wrong delimiters with multiple negatives"""
        with self.assertRaises(ValueError) as context:
            add("//;\n-1,2;-3\n-4")
        error_msg = str(context.exception)
        self.assertIn("';' expected but ',' found", error_msg)
        self.assertIn("Negative number(s) not allowed: -1, -3, -4", error_msg)


if __name__ == "__main__":
    unittest.main()
