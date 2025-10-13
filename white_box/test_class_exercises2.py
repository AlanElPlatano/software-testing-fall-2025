# -*- coding: utf-8 -*-

"""
White-box unit testing examples
Tests for exercises 11-21, 24, and 26
On a separate file because i refuse to have 1000-something lines of code in a single file
"""
import unittest

from white_box.class_exercises import (
    ElevatorSystem,
    UserAuthentication,
    authenticate_user,
    calculate_quantity_discount,
    calculate_shipping_cost,
    check_file_size,
    check_flight_eligibility,
    check_loan_eligibility,
    get_weather_advisory,
    grade_quiz,
    validate_credit_card,
    validate_date,
    validate_url,
)


class TestWhiteBoxExtended(unittest.TestCase):
    """
    White-box unittest class for exercises 11-21.
    """

    # 11
    def test_validate_credit_card_valid_min_length(self):
        """
        Checks valid credit card with minimum length (13 digits)
        """
        self.assertEqual(validate_credit_card("1234567890123"), "Valid Card")

    def test_validate_credit_card_valid_max_length(self):
        """
        Checks valid credit card with maximum length (16 digits)
        """
        self.assertEqual(validate_credit_card("1234567890123456"), "Valid Card")

    def test_validate_credit_card_valid_mid_length(self):
        """
        Checks valid credit card with middle length (14 digits)
        """
        self.assertEqual(validate_credit_card("12345678901234"), "Valid Card")

    def test_validate_credit_card_too_short(self):
        """
        Checks credit card with less than 13 digits is invalid
        """
        self.assertEqual(validate_credit_card("123456789012"), "Invalid Card")

    def test_validate_credit_card_too_long(self):
        """
        Checks credit card with more than 16 digits is invalid
        """
        self.assertEqual(validate_credit_card("12345678901234567"), "Invalid Card")

    def test_validate_credit_card_non_digit(self):
        """
        Checks credit card with non-digit characters is invalid
        """
        self.assertEqual(validate_credit_card("1234567890abc"), "Invalid Card")

    def test_validate_credit_card_with_spaces(self):
        """
        Checks credit card with spaces is invalid
        """
        self.assertEqual(validate_credit_card("1234 5678 9012 3456"), "Invalid Card")

    # 12
    # check year, month, and day ranges independently
    def test_validate_date_valid_min_year(self):
        """
        Checks valid date with minimum year (1900)
        """
        self.assertEqual(validate_date(1900, 1, 1), "Valid Date")

    def test_validate_date_valid_max_year(self):
        """
        Checks valid date with maximum year (2100)
        """
        self.assertEqual(validate_date(2100, 12, 31), "Valid Date")

    def test_validate_date_valid_middle(self):
        """
        Checks valid date in the middle of range
        """
        self.assertEqual(validate_date(2000, 6, 15), "Valid Date")

    def test_validate_date_year_too_low(self):
        """
        Checks date with year below 1900 is invalid
        """
        self.assertEqual(validate_date(1899, 1, 1), "Invalid Date")

    def test_validate_date_year_too_high(self):
        """
        Checks date with year above 2100 is invalid
        """
        self.assertEqual(validate_date(2101, 1, 1), "Invalid Date")

    def test_validate_date_month_too_low(self):
        """
        Checks date with month below 1 is invalid
        """
        self.assertEqual(validate_date(2000, 0, 15), "Invalid Date")

    def test_validate_date_month_too_high(self):
        """
        Checks date with month above 12 is invalid
        """
        self.assertEqual(validate_date(2000, 13, 15), "Invalid Date")

    def test_validate_date_day_too_low(self):
        """
        Checks date with day below 1 is invalid
        """
        self.assertEqual(validate_date(2000, 6, 0), "Invalid Date")

    def test_validate_date_day_too_high(self):
        """
        Checks date with day above 31 is invalid
        """
        self.assertEqual(validate_date(2000, 6, 32), "Invalid Date")

    # 13
    # As long as either age range or frequent flyer status are true, that makes you eligible
    def test_check_flight_eligibility_age_in_range_not_frequent(self):
        """
        Checks eligibility for age within range (18-65) and not frequent flyer
        """
        self.assertEqual(check_flight_eligibility(30, False), "Eligible to Book")

    def test_check_flight_eligibility_age_min_boundary(self):
        """
        Checks eligibility for minimum age boundary (18)
        """
        self.assertEqual(check_flight_eligibility(18, False), "Eligible to Book")

    def test_check_flight_eligibility_age_max_boundary(self):
        """
        Checks eligibility for maximum age boundary (65)
        """
        self.assertEqual(check_flight_eligibility(65, False), "Eligible to Book")

    def test_check_flight_eligibility_too_young_not_frequent(self):
        """
        Checks not eligible for age below 18 and not frequent flyer
        """
        self.assertEqual(check_flight_eligibility(17, False), "Not Eligible to Book")

    def test_check_flight_eligibility_too_old_not_frequent(self):
        """
        Checks not eligible for age above 65 and not frequent flyer
        """
        self.assertEqual(check_flight_eligibility(66, False), "Not Eligible to Book")

    def test_check_flight_eligibility_too_young_frequent_flyer(self):
        """
        Checks eligible for age below 18 but frequent flyer
        """
        self.assertEqual(
            check_flight_eligibility(17, True), "Eligible to Book"
        )  # Frequent flyter status is more important than age

    def test_check_flight_eligibility_too_old_frequent_flyer(self):
        """
        Checks eligible for age above 65 but frequent flyer
        """
        self.assertEqual(check_flight_eligibility(66, True), "Eligible to Book")

    def test_check_flight_eligibility_in_range_frequent_flyer(self):
        """
        Checks eligible for age in range and frequent flyer
        """
        self.assertEqual(check_flight_eligibility(30, True), "Eligible to Book")

    # 14
    def test_validate_url_valid_http(self):
        """
        Checks valid URL starting with http://
        """
        self.assertEqual(validate_url("http://example.com"), "Valid URL")

    def test_validate_url_valid_https(self):
        """
        Checks valid URL starting with https://
        """
        self.assertEqual(validate_url("https://example.com"), "Valid URL")

    def test_validate_url_valid_max_length(self):
        """
        Checks valid URL at maximum length (255 characters)
        """
        url = "https://" + "a" * 247  # Exactly 255 characters total
        self.assertEqual(validate_url(url), "Valid URL")

    def test_validate_url_too_long(self):
        """
        Checks URL longer than 255 characters is invalid
        """
        url = "https://" + "a" * 248  # 256 characters which is over the limit
        self.assertEqual(validate_url(url), "Invalid URL")

    def test_validate_url_no_protocol(self):
        """
        Checks URL without http:// or https:// is invalid
        """
        self.assertEqual(validate_url("example.com"), "Invalid URL")

    def test_validate_url_wrong_protocol(self):
        """
        Checks URL with wrong protocol (ftp://) is invalid
        """
        self.assertEqual(validate_url("ftp://example.com"), "Invalid URL")

    # 15
    def test_calculate_quantity_discount_no_discount_min(self):
        """
        Checks no discount for quantity 1
        """
        self.assertEqual(calculate_quantity_discount(1), "No Discount")

    def test_calculate_quantity_discount_no_discount_max(self):
        """
        Checks no discount for quantity 5
        """
        self.assertEqual(calculate_quantity_discount(5), "No Discount")

    def test_calculate_quantity_discount_5_percent_min(self):
        """
        Checks 5% discount for quantity 6
        """
        self.assertEqual(calculate_quantity_discount(6), "5% Discount")

    def test_calculate_quantity_discount_5_percent_max(self):
        """
        Checks 5% discount for quantity 10
        """
        self.assertEqual(calculate_quantity_discount(10), "5% Discount")

    def test_calculate_quantity_discount_10_percent(self):
        """
        Checks 10% discount for quantity above 10
        """
        self.assertEqual(calculate_quantity_discount(11), "10% Discount")

    def test_calculate_quantity_discount_zero(self):
        """
        Checks quantity 0 returns 10% discount (outside 1-10 range)
        """
        self.assertEqual(calculate_quantity_discount(0), "10% Discount")

    # 16
    def test_check_file_size_valid_zero(self):
        """
        Checks file size of 0 bytes is valid
        """
        self.assertEqual(check_file_size(0), "Valid File Size")

    def test_check_file_size_valid_max(self):
        """
        Checks file size of 1 MB (1048576 bytes) is valid
        """
        self.assertEqual(check_file_size(1048576), "Valid File Size")

    def test_check_file_size_valid_middle(self):
        """
        Checks file size in middle of range is valid
        """
        self.assertEqual(check_file_size(500000), "Valid File Size")

    def test_check_file_size_negative(self):
        """
        Checks negative file size is invalid
        """
        self.assertEqual(check_file_size(-1), "Invalid File Size")

    def test_check_file_size_too_large(self):
        """
        Checks file size above 1 MB is invalid
        """
        self.assertEqual(check_file_size(1048577), "Invalid File Size")

    # 17
    # This function has nested conditions so many tests came out of it
    def test_check_loan_eligibility_income_too_low(self):
        """
        Checks not eligible for income below 30000
        """
        self.assertEqual(check_loan_eligibility(29999, 800), "Not Eligible")

    def test_check_loan_eligibility_standard_loan_good_credit(self):
        """
        Checks standard loan for income 30000-60000 with credit score > 700
        """
        self.assertEqual(check_loan_eligibility(50000, 750), "Standard Loan")

    def test_check_loan_eligibility_secured_loan_low_credit(self):
        """
        Checks secured loan for income 30000-60000 with credit score <= 700
        """
        self.assertEqual(check_loan_eligibility(50000, 700), "Secured Loan")

    def test_check_loan_eligibility_secured_loan_very_low_credit(self):
        """
        Checks secured loan for income 30000-60000 with low credit score
        """
        self.assertEqual(check_loan_eligibility(50000, 600), "Secured Loan")

    def test_check_loan_eligibility_premium_loan(self):
        """
        Checks premium loan for income > 60000 with credit score > 750
        """
        self.assertEqual(
            check_loan_eligibility(70000, 800), "Premium Loan"
        )  # high income + high credit

    def test_check_loan_eligibility_high_income_low_credit(self):
        """
        Checks standard loan for income > 60000 with credit score <= 750
        """
        self.assertEqual(check_loan_eligibility(70000, 750), "Standard Loan")

    def test_check_loan_eligibility_boundary_income_min(self):
        """
        Checks loan at minimum income boundary (30000) with good credit
        """
        self.assertEqual(check_loan_eligibility(30000, 750), "Standard Loan")

    def test_check_loan_eligibility_boundary_income_max(self):
        """
        Checks loan at maximum income boundary (60000) with good credit
        """
        self.assertEqual(check_loan_eligibility(60000, 750), "Standard Loan")

    # 18
    # Here weight, length, width, height all matter so many tests occured to me here
    def test_calculate_shipping_cost_small_package(self):
        """
        Checks shipping cost $5 for small package (weight<=1, dimensions<=10)
        """
        self.assertEqual(calculate_shipping_cost(1, 10, 10, 10), 5)

    def test_calculate_shipping_cost_medium_package(self):
        """
        Checks shipping cost $10 for medium package
        """
        self.assertEqual(calculate_shipping_cost(3, 20, 20, 20), 10)

    def test_calculate_shipping_cost_large_package(self):
        """
        Checks shipping cost $20 for large package
        """
        self.assertEqual(calculate_shipping_cost(10, 50, 50, 50), 20)

    def test_calculate_shipping_cost_weight_exceeds_small(self):
        """
        Checks shipping cost $20 when weight > 1 but dimensions small
        """
        self.assertEqual(calculate_shipping_cost(2, 10, 10, 10), 20)

    def test_calculate_shipping_cost_length_exceeds_small(self):
        """
        Checks shipping cost $20 when length > 10 but other dimensions small
        """
        self.assertEqual(calculate_shipping_cost(1, 11, 10, 10), 20)

    def test_calculate_shipping_cost_width_exceeds_small(self):
        """
        Checks shipping cost $20 when width > 10 but other dimensions small
        """
        self.assertEqual(calculate_shipping_cost(1, 10, 11, 10), 20)

    def test_calculate_shipping_cost_height_exceeds_small(self):
        """
        Checks shipping cost $20 when height > 10 but other dimensions small
        """
        self.assertEqual(calculate_shipping_cost(1, 10, 10, 11), 20)

    def test_calculate_shipping_cost_weight_exceeds_medium(self):
        """
        Checks shipping cost $20 when weight > 5
        """
        self.assertEqual(calculate_shipping_cost(6, 20, 20, 20), 20)

    # 19
    # test both correct and incorrect answer combinations
    def test_grade_quiz_pass(self):
        """
        Checks Pass for 7+ correct and <=2 incorrect
        """
        self.assertEqual(grade_quiz(7, 2), "Pass")

    def test_grade_quiz_pass_perfect(self):
        """
        Checks Pass for 10 correct and 0 incorrect
        """
        self.assertEqual(grade_quiz(10, 0), "Pass")

    def test_grade_quiz_conditional_pass_min(self):
        """
        Checks Conditional Pass for 5 correct and <=3 incorrect
        """
        self.assertEqual(grade_quiz(5, 3), "Conditional Pass")

    def test_grade_quiz_conditional_pass_6_correct(self):
        """
        Checks Conditional Pass for 6 correct and 3 incorrect
        """
        self.assertEqual(grade_quiz(6, 3), "Conditional Pass")

    def test_grade_quiz_fail_too_few_correct(self):
        """
        Checks Fail for less than 5 correct answers
        """
        self.assertEqual(grade_quiz(4, 2), "Fail")

    def test_grade_quiz_fail_too_many_incorrect(self):
        """
        Checks Fail for 5 correct but > 3 incorrect
        """
        self.assertEqual(grade_quiz(5, 4), "Fail")

    def test_grade_quiz_fail_7_correct_too_many_incorrect(self):
        """
        Checks Fail for 7 correct but > 2 incorrect
        """
        self.assertEqual(grade_quiz(7, 3), "Fail")

    # 20
    # admin has hardcoded credentials but other users just need length requirements
    def test_authenticate_user_admin_success(self):
        """
        Checks admin authentication with correct credentials
        """
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")

    def test_authenticate_user_admin_wrong_password(self):
        """
        Checks admin authentication fails with wrong password
        """
        self.assertEqual(authenticate_user("admin", "wrongpass"), "Invalid")

    def test_authenticate_user_valid_user(self):
        """
        Checks valid user with username >= 5 and password >= 8
        """
        self.assertEqual(authenticate_user("user123", "password"), "User")

    def test_authenticate_user_username_too_short(self):
        """
        Checks invalid user with username < 5 characters
        """
        self.assertEqual(authenticate_user("user", "password"), "Invalid")

    def test_authenticate_user_password_too_short(self):
        """
        Checks invalid user with password < 8 characters
        """
        self.assertEqual(authenticate_user("user123", "pass"), "Invalid")

    def test_authenticate_user_both_too_short(self):
        """
        Checks invalid user with both username and password too short
        """
        self.assertEqual(authenticate_user("user", "pass"), "Invalid")

    def test_authenticate_user_boundary_min(self):
        """
        Checks valid user at minimum boundary (username=5, password=8)
        """
        self.assertEqual(authenticate_user("user1", "password"), "User")

    # 21
    def test_get_weather_advisory_high_temp_high_humidity(self):
        """
        Checks advisory for temperature > 30 and humidity > 70
        """
        self.assertEqual(
            get_weather_advisory(35, 80),
            "High Temperature and Humidity. Stay Hydrated.",
        )

    def test_get_weather_advisory_high_temp_low_humidity(self):
        """
        Checks no specific advisory for temperature > 30 but humidity <= 70
        """
        self.assertEqual(get_weather_advisory(35, 50), "No Specific Advisory")

    def test_get_weather_advisory_low_temp(self):
        """
        Checks advisory for temperature < 0
        """
        self.assertEqual(get_weather_advisory(-5, 50), "Low Temperature. Bundle Up!")

    def test_get_weather_advisory_low_temp_high_humidity(self):
        """
        Checks low temperature advisory takes precedence
        """
        self.assertEqual(get_weather_advisory(-5, 80), "Low Temperature. Bundle Up!")

    def test_get_weather_advisory_normal_conditions(self):
        """
        Checks no specific advisory for normal conditions
        """
        self.assertEqual(get_weather_advisory(20, 60), "No Specific Advisory")

    def test_get_weather_advisory_boundary_temp_30(self):
        """
        Checks no specific advisory for temperature exactly 30
        """
        self.assertEqual(get_weather_advisory(30, 80), "No Specific Advisory")

    def test_get_weather_advisory_boundary_humidity_70(self):
        """
        Checks no specific advisory for humidity exactly 70
        """
        self.assertEqual(get_weather_advisory(35, 70), "No Specific Advisory")

    def test_get_weather_advisory_boundary_temp_0(self):
        """
        Checks no specific advisory for temperature exactly 0
        """
        self.assertEqual(get_weather_advisory(0, 50), "No Specific Advisory")


# 24
class TestUserAuthentication(unittest.TestCase):
    """
    Unit tests for UserAuthentication class (exercise 24).
    """

    def setUp(self):
        """
        Set up a new UserAuthentication instance for each test
        """
        self.auth = UserAuthentication()

    def test_initial_state_logged_out(self):
        """
        Checks that initial state is Logged Out
        """
        self.assertEqual(self.auth.state, "Logged Out")

    def test_login_success(self):
        """
        Checks successful login from Logged Out state
        """
        result = self.auth.login()
        self.assertEqual(result, "Login successful")
        self.assertEqual(self.auth.state, "Logged In")

    def test_login_already_logged_in(self):
        """
        Checks login fails when already logged in
        """
        self.auth.login()  # First login
        result = self.auth.login()  # Try to login again
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.auth.state, "Logged In")

    def test_logout_success(self):
        """
        Checks successful logout from Logged In state
        """
        self.auth.login()  # Login first
        result = self.auth.logout()
        self.assertEqual(result, "Logout successful")
        self.assertEqual(self.auth.state, "Logged Out")

    def test_logout_already_logged_out(self):
        """
        Checks logout fails when already logged out
        """
        result = self.auth.logout()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.auth.state, "Logged Out")

    def test_login_logout_cycle(self):
        """
        Checks full login-logout cycle works correctly
        """
        # Login
        self.auth.login()
        self.assertEqual(self.auth.state, "Logged In")
        # Logout
        self.auth.logout()
        self.assertEqual(self.auth.state, "Logged Out")
        # Login again
        result = self.auth.login()
        self.assertEqual(result, "Login successful")
        self.assertEqual(self.auth.state, "Logged In")


# 26
class TestElevatorSystem(unittest.TestCase):
    """
    Unit tests for ElevatorSystem class (exercise 26).
    """

    def setUp(self):
        """
        Set up a new ElevatorSystem instance for each test
        """
        self.elevator = ElevatorSystem()

    def test_initial_state_idle(self):
        """
        Checks that initial state is Idle
        """
        self.assertEqual(self.elevator.state, "Idle")

    def test_move_up_from_idle(self):
        """
        Checks elevator can move up from Idle state
        """
        result = self.elevator.move_up()
        self.assertEqual(result, "Elevator moving up")
        self.assertEqual(self.elevator.state, "Moving Up")

    def test_move_down_from_idle(self):
        """
        Checks elevator can move down from Idle state
        """
        result = self.elevator.move_down()
        self.assertEqual(result, "Elevator moving down")
        self.assertEqual(self.elevator.state, "Moving Down")

    def test_move_up_from_moving_up(self):
        """
        Checks move_up fails when already moving up
        """
        self.elevator.move_up()  # Start moving up
        result = self.elevator.move_up()  # Try to move up again
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.elevator.state, "Moving Up")

    def test_move_down_from_moving_down(self):
        """
        Checks move_down fails when already moving down
        """
        self.elevator.move_down()  # Start moving down
        result = self.elevator.move_down()  # Try to move down again
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.elevator.state, "Moving Down")

    def test_move_up_from_moving_down(self):
        """
        Checks move_up fails when moving down
        """
        self.elevator.move_down()  # Can't change direction while moving
        result = self.elevator.move_up()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.elevator.state, "Moving Down")

    def test_move_down_from_moving_up(self):
        """
        Checks move_down fails when moving up
        """
        self.elevator.move_up()  # Same here - need to stop first
        result = self.elevator.move_down()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.elevator.state, "Moving Up")

    def test_stop_from_moving_up(self):
        """
        Checks elevator can stop from Moving Up state
        """
        self.elevator.move_up()
        result = self.elevator.stop()
        self.assertEqual(result, "Elevator stopped")
        self.assertEqual(self.elevator.state, "Idle")

    def test_stop_from_moving_down(self):
        """
        Checks elevator can stop from Moving Down state
        """
        self.elevator.move_down()
        result = self.elevator.stop()
        self.assertEqual(result, "Elevator stopped")
        self.assertEqual(self.elevator.state, "Idle")

    def test_stop_from_idle(self):
        """
        Checks stop fails when already idle
        """
        result = self.elevator.stop()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.elevator.state, "Idle")

    def test_move_up_stop_move_down_cycle(self):
        """
        Checks complete cycle: move up, stop, move down, stop
        """
        # Move up
        self.elevator.move_up()
        self.assertEqual(self.elevator.state, "Moving Up")
        # Stop
        self.elevator.stop()
        self.assertEqual(self.elevator.state, "Idle")
        # Move down
        self.elevator.move_down()
        self.assertEqual(self.elevator.state, "Moving Down")
        # Stop
        self.elevator.stop()
        self.assertEqual(self.elevator.state, "Idle")
