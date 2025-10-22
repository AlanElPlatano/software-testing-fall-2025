# -*- coding: utf-8 -*-

# python -m unittest tdd.test_fb

"""
White-box unit testing examples.
"""
import unittest

from tdd.fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    """Unit tests for the fizzbuzz function."""

    # Test several numbers that should return fizz
    def test_fizz(self):
        """Test that numbers divisible by 3 (but not 5) return 'Fizz'."""
        self.assertEqual(fizzbuzz(3), ["Fizz"])
        self.assertEqual(fizzbuzz(6), ["Fizz"])
        self.assertEqual(fizzbuzz(9), ["Fizz"])

    # Test several numbers that should return buzz
    def test_buzz(self):
        """Test that numbers divisible by 5 (but not 3) return 'Buzz'."""
        self.assertEqual(fizzbuzz(5), ["Buzz"])
        self.assertEqual(fizzbuzz(10), ["Buzz"])
        self.assertEqual(fizzbuzz(20), ["Buzz"])

    # Test several numbers that should return fizzbuzz
    def test_fizzbuzz(self):
        """Test that numbers divisible by both 3 and 5 return 'FizzBuzz'."""
        self.assertEqual(fizzbuzz(15), ["FizzBuzz"])
        self.assertEqual(fizzbuzz(30), ["FizzBuzz"])
        self.assertEqual(fizzbuzz(45), ["FizzBuzz"])

    # Test several numbers that should return neither
    def test_neither(self):
        """Test that numbers not divisible by 3 or 5 return None."""
        self.assertIsNone(fizzbuzz(1))
        self.assertIsNone(fizzbuzz(2))
        self.assertIsNone(fizzbuzz(4))
        self.assertIsNone(fizzbuzz(7))
