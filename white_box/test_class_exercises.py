# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from white_box.class_exercises import (
    TrafficLight,
    VendingMachine,
    calculate_items_shipping_cost,
    calculate_order_total,
    calculate_total_discount,
    categorize_product,
    celsius_to_fahrenheit,
    check_number_status,
    divide,
    get_grade,
    is_even,
    is_triangle,
    validate_email,
    validate_login,
    validate_password,
    verify_age,
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

    # 4
    def test_calculate_order_total_quantity_1_to_5(self):
        """
        Checks that items with quantity 1-5 get no discount
        """
        items = [{"quantity": 3, "price": 10.0}]
        self.assertEqual(calculate_order_total(items), 30.0)

    def test_calculate_order_total_quantity_6_to_10(self):
        """
        Checks that items with quantity 6-10 get 5% discount
        """
        items = [{"quantity": 8, "price": 10.0}]
        self.assertEqual(calculate_order_total(items), 76.0)

    def test_calculate_order_total_quantity_above_10(self):
        """
        Checks that items with quantity above 10 get 10% discount
        """
        items = [{"quantity": 15, "price": 10.0}]
        self.assertEqual(calculate_order_total(items), 135.0)

    def test_calculate_order_total_multiple_items(self):
        """
        Checks total calculation with multiple items in different quantity ranges
        """
        items = [
            {"quantity": 2, "price": 10.0},  # 20.0
            {"quantity": 7, "price": 5.0},  # 33.25 (5% discount)
            {"quantity": 12, "price": 8.0},  # 86.4 (10% discount)
        ]
        self.assertEqual(calculate_order_total(items), 139.65)

    def test_calculate_order_total_empty_list(self):
        """
        Checks that empty items list returns 0
        """
        items = []
        self.assertEqual(calculate_order_total(items), 0)

    # 5
    def test_shipping_standard_weight_0_to_5(self):
        """
        Checks standard shipping cost for weight <= 5
        """
        items = [{"weight": 3}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_shipping_standard_weight_5_to_10(self):
        """
        Checks standard shipping cost for weight > 5 and <= 10
        """
        items = [{"weight": 7}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)

    def test_shipping_standard_weight_above_10(self):
        """
        Checks standard shipping cost for weight > 10
        """
        items = [{"weight": 12}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 20)

    def test_shipping_express_weight_0_to_5(self):
        """
        Checks express shipping cost for weight <= 5
        """
        items = [{"weight": 4}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

    def test_shipping_express_weight_5_to_10(self):
        """
        Checks express shipping cost for weight > 5 and <= 10
        """
        items = [{"weight": 8}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)

    def test_shipping_express_weight_above_10(self):
        """
        Checks express shipping cost for weight > 10
        """
        items = [{"weight": 15}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 40)

    def test_shipping_invalid_method(self):
        """
        Checks that invalid shipping method raises ValueError
        """
        items = [{"weight": 5}]
        with self.assertRaises(ValueError):
            calculate_items_shipping_cost(items, "overnight")

    def test_shipping_multiple_items(self):
        """
        Checks shipping cost calculation with multiple items
        """
        items = [{"weight": 2}, {"weight": 3}, {"weight": 2}]  # total weight = 7
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)

    # 6
    def test_validate_login_success(self):
        """
        Checks successful login with valid username and password lengths
        """
        self.assertEqual(validate_login("user123", "password1"), "Login Successful")

    def test_validate_login_username_too_short(self):
        """
        Checks login fails when username is less than 5 characters
        """
        self.assertEqual(validate_login("usr", "password1"), "Login Failed")

    def test_validate_login_username_too_long(self):
        """
        Checks login fails when username is more than 20 characters
        """
        self.assertEqual(validate_login("a" * 21, "password1"), "Login Failed")

    def test_validate_login_password_too_short(self):
        """
        Checks login fails when password is less than 8 characters
        """
        self.assertEqual(validate_login("user123", "pass"), "Login Failed")

    def test_validate_login_password_too_long(self):
        """
        Checks login fails when password is more than 15 characters
        """
        self.assertEqual(validate_login("user123", "a" * 16), "Login Failed")

    def test_validate_login_boundary_min(self):
        """
        Checks login succeeds at minimum boundary (username=5, password=8)
        """
        self.assertEqual(validate_login("user1", "password"), "Login Successful")

    def test_validate_login_boundary_max(self):
        """
        Checks login succeeds at maximum boundary (username=20, password=15)
        """
        self.assertEqual(validate_login("a" * 20, "a" * 15), "Login Successful")

    # 7
    def test_verify_age_eligible_min(self):
        """
        Checks age 18 (minimum boundary) is eligible
        """
        self.assertEqual(verify_age(18), "Eligible")

    def test_verify_age_eligible_max(self):
        """
        Checks age 65 (maximum boundary) is eligible
        """
        self.assertEqual(verify_age(65), "Eligible")

    def test_verify_age_eligible_middle(self):
        """
        Checks age within range is eligible
        """
        self.assertEqual(verify_age(40), "Eligible")

    def test_verify_age_not_eligible_too_young(self):
        """
        Checks age below 18 is not eligible
        """
        self.assertEqual(verify_age(17), "Not Eligible")

    def test_verify_age_not_eligible_too_old(self):
        """
        Checks age above 65 is not eligible
        """
        self.assertEqual(verify_age(66), "Not Eligible")

    # 8
    def test_categorize_product_category_a_min(self):
        """
        Checks price 10 (minimum boundary) returns Category A
        """
        self.assertEqual(categorize_product(10), "Category A")

    def test_categorize_product_category_a_max(self):
        """
        Checks price 50 (maximum boundary) returns Category A
        """
        self.assertEqual(categorize_product(50), "Category A")

    def test_categorize_product_category_b_min(self):
        """
        Checks price 51 (minimum boundary) returns Category B
        """
        self.assertEqual(categorize_product(51), "Category B")

    def test_categorize_product_category_b_max(self):
        """
        Checks price 100 (maximum boundary) returns Category B
        """
        self.assertEqual(categorize_product(100), "Category B")

    def test_categorize_product_category_c_min(self):
        """
        Checks price 101 (minimum boundary) returns Category C
        """
        self.assertEqual(categorize_product(101), "Category C")

    def test_categorize_product_category_c_max(self):
        """
        Checks price 200 (maximum boundary) returns Category C
        """
        self.assertEqual(categorize_product(200), "Category C")

    def test_categorize_product_category_d_below(self):
        """
        Checks price below 10 returns Category D
        """
        self.assertEqual(categorize_product(5), "Category D")

    def test_categorize_product_category_d_above(self):
        """
        Checks price above 200 returns Category D
        """
        self.assertEqual(categorize_product(250), "Category D")

    # 9
    def test_validate_email_valid(self):
        """
        Checks valid email with @ and . within length bounds
        """
        self.assertEqual(validate_email("user@example.com"), "Valid Email")

    def test_validate_email_too_short(self):
        """
        Checks email shorter than 5 characters is invalid
        """
        self.assertEqual(validate_email("a@b"), "Invalid Email")

    def test_validate_email_too_long(self):
        """
        Checks email longer than 50 characters is invalid
        """
        self.assertEqual(
            validate_email("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"),
            "Invalid Email",
        )  # A lot of letters

    def test_validate_email_no_at_symbol(self):
        """
        Checks email without @ symbol is invalid
        """
        self.assertEqual(validate_email("userexample.com"), "Invalid Email")

    def test_validate_email_no_dot(self):
        """
        Checks email without . symbol is invalid
        """
        self.assertEqual(validate_email("user@examplecom"), "Invalid Email")

    def test_validate_email_boundary_min(self):
        """
        Checks email at minimum length (5) with @ and . is valid
        """
        self.assertEqual(validate_email("a@b.c"), "Valid Email")

    def test_validate_email_boundary_max(self):
        """
        Checks email at maximum length (50) with @ and . is valid
        """
        long_email = (
            "user@"
            + "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            + ".com"
        )  # A lof of letters
        self.assertEqual(validate_email(long_email), "Valid Email")

    # 10
    def test_celsius_to_fahrenheit_zero(self):
        """
        Checks conversion of 0°C to 32°F
        """
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)

    def test_celsius_to_fahrenheit_positive(self):
        """
        Checks conversion of positive temperature (25°C to 77°F)
        """
        self.assertEqual(celsius_to_fahrenheit(25), 77.0)

    def test_celsius_to_fahrenheit_negative(self):
        """
        Checks conversion of negative temperature (-40°C to -40°F)
        """
        self.assertEqual(celsius_to_fahrenheit(-40), -40.0)

    def test_celsius_to_fahrenheit_boundary_min(self):
        """
        Checks conversion at minimum boundary (-100°C)
        """
        self.assertEqual(celsius_to_fahrenheit(-100), -148.0)

    def test_celsius_to_fahrenheit_boundary_max(self):
        """
        Checks conversion at maximum boundary (100°C to 212°F)
        """
        self.assertEqual(celsius_to_fahrenheit(100), 212.0)

    def test_celsius_to_fahrenheit_below_min(self):
        """
        Checks temperature below -100°C returns invalid
        """
        self.assertEqual(celsius_to_fahrenheit(-101), "Invalid Temperature")

    def test_celsius_to_fahrenheit_above_max(self):
        """
        Checks temperature above 100°C returns invalid
        """
        self.assertEqual(celsius_to_fahrenheit(101), "Invalid Temperature")

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
        light.change_state()  # Red to Green
        light.change_state()  # Green to Yellow
        light.change_state()  # Yellow to Red
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
