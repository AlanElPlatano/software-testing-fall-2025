# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from white_box.class_exercises import (
    TrafficLight,
    VendingMachine,
    calculate_total_discount,
    check_number_status,
    divide,
    get_grade,
    is_even,
    is_triangle,
    validate_password,
)


class TestWhiteBox(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_is_even_with_even_number(self):
        """
        Checks if a number is even.
        """
        self.assertTrue(is_even(0))

    def test_is_even_with_odd_number(self):
        """
        Checks if a number is not even.
        """
        self.assertFalse(is_even(7))

    def test_divide_by_non_zero(self):
        """
        Checks the divide function works as expected.
        """
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        """
        Checks the divide function returns 0 when dividing by 0.
        """
        self.assertEqual(divide(10, 0), 0)

    def test_get_grade_a(self):
        """
        Checks A grade.
        """
        self.assertEqual(get_grade(95), "A")

    def test_get_grade_b(self):
        """
        Checks B grade.
        """
        self.assertEqual(get_grade(85), "B")

    def test_get_grade_c(self):
        """
        Checks C grade.
        """
        self.assertEqual(get_grade(75), "C")

    def test_get_grade_f(self):
        """
        Checks F grade.
        """
        self.assertEqual(get_grade(65), "F")

    def test_is_triangle_yes(self):
        """
        Checks the three inputs can form a triangle.
        """
        self.assertEqual(is_triangle(3, 4, 5), "Yes, it's a triangle!")

    def test_is_triangle_no_1(self):
        """
        Checks the three inputs can't form a triangle when C is greater or equal than A + B.
        """
        self.assertEqual(is_triangle(3, 4, 7), "No, it's not a triangle.")

    def test_is_triangle_no_2(self):
        """
        Checks the three inputs can't form a triangle when B is greater or equal than A + C.
        """
        self.assertEqual(is_triangle(2, 3, 1), "No, it's not a triangle.")

    def test_is_triangle_no_3(self):
        """
        Checks the three inputs can't form a triangle when A is greater or equal than B + C.
        """
        self.assertEqual(is_triangle(2, 1, 1), "No, it's not a triangle.")

    # 1
    def test_check_number_status_1(self):
        """
        Checks the first possible outcome of the function with a positive value
        """
        self.assertEqual(check_number_status(1), "Positive")

    def test_check_number_status_2(self):
        """
        Checks the first possible outcome of the function with a negative value
        """
        self.assertEqual(check_number_status(-1), "Negative")

    def test_check_number_status_3(self):
        """
        Checks the first possible outcome of the function with a zero value
        """
        self.assertEqual(check_number_status(0), "Zero")

    # 2
    def test_validate_password_too_short(self):
        """
        Checks the validate_password function with a length below 8
        """
        self.assertEqual(validate_password("Ab1!"), False)

    def test_validate_password_no_uppercase(self):
        """
        Checks the validate_password function with no uppercase letters
        """
        self.assertEqual(validate_password("password1!"), False)

    def test_validate_password_no_lowercase(self):
        """
        Checks the validate_password function with no lowercase letters
        """
        self.assertEqual(validate_password("PASSWORD1!"), False)

    def test_validate_password_no_digit(self):
        """
        Checks the validate_password function with no digits
        """
        self.assertEqual(validate_password("Password!"), False)

    def test_validate_password_no_special_char(self):
        """
        Checks the validate_password function with no special characters
        """
        self.assertEqual(validate_password("Password1"), False)

    def test_validate_password_valid(self):
        """
        Checks the validate_password function with a valid password
        """
        self.assertEqual(validate_password("Password1!"), True)

    # 3
    def test_calculate_total_discount_below_100(self):
        """
        Checks that amounts below 100 get no discount
        """
        self.assertEqual(calculate_total_discount(50), 0)

    def test_calculate_total_discount_exactly_100(self):
        """
        Checks that amount exactly 100 gets 10% discount
        """
        self.assertEqual(calculate_total_discount(100), 10.0)

    def test_calculate_total_discount_between_100_and_500(self):
        """
        Checks that amounts between 100 and 500 get 10% discount
        """
        self.assertEqual(calculate_total_discount(250), 25.0)

    def test_calculate_total_discount_exactly_500(self):
        """
        Checks that amount exactly 500 gets 10% discount
        """
        self.assertEqual(calculate_total_discount(500), 50.0)

    def test_calculate_total_discount_above_500(self):
        """
        Checks that amounts above 500 get 20% discount
        """
        self.assertEqual(calculate_total_discount(600), 120.0)

    # 23
    def test_initial_state(self):
        """
        Checks that the initial state of the TrafficLight is Red
        """
        light = TrafficLight()
        self.assertEqual(light.get_current_state(), "Red")

    def test_change_state_red_to_green(self):
        """
        Checks that state changes from Red to Green
        """
        light = TrafficLight()
        light.change_state()
        self.assertEqual(light.get_current_state(), "Green")

    def test_change_state_green_to_yellow(self):
        """
        Checks that state changes from Green to Yellow
        """
        light = TrafficLight()
        light.state = "Green"  # force state
        light.change_state()
        self.assertEqual(light.get_current_state(), "Yellow")

    def test_change_state_yellow_to_red(self):
        """
        Checks that state changes from Yellow to Red
        """
        light = TrafficLight()
        light.state = "Yellow"  # force state
        light.change_state()
        self.assertEqual(light.get_current_state(), "Red")

    def test_full_cycle(self):
        """
        Checks that the traffic light cycles through Red → Green → Yellow → Red
        """
        light = TrafficLight()
        light.change_state()  # Red → Green
        light.change_state()  # Green → Yellow
        light.change_state()  # Yellow → Red
        self.assertEqual(light.get_current_state(), "Red")


class TestWhiteBoxVendingMachine(unittest.TestCase):
    """
    Vending Machine unit tests.
    """

    # @classmethod
    # def setUpClass(cls):
    #    return

    def setUp(self):
        self.vending_machine = VendingMachine()
        self.assertEqual(self.vending_machine.state, "Ready")

    # def tearDown(self):
    #    return

    # @classmethod
    # def tearDownClass(cls):
    #    return

    def test_vending_machine_insert_coin_error(self):
        """
        Checks the vending machine can accept coins.
        """
        self.vending_machine.state = "Dispensing"

        output = self.vending_machine.insert_coin()

        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Invalid operation in current state.")

    def test_vending_machine_insert_coin_success(self):
        """
        Checks the vending machine fails to accept coins when it's not ready.
        """
        output = self.vending_machine.insert_coin()

        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Coin Inserted. Select your drink.")
