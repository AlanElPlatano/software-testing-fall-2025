# -*- coding: utf-8 -*-
"""
Mock up testing examples for BankingSystem.
"""
import unittest
from unittest.mock import MagicMock, patch

from white_box.class_exercises import BankAccount, BankingSystem


# 27
class TestBankAccount(unittest.TestCase):
    """
    BankAccount unittest class.
    """

    def test_view_account(self):
        """
        Test view_account displays correct information.
        """
        # Create a bank account instance
        account = BankAccount("ACC001", 5000)

        # Assert the return value is correct
        self.assertEqual(
            account.view_account(), "The account ACC001 has a balance of 5000"
        )


class TestBankingSystem(unittest.TestCase):
    """
    BankingSystem unittest class.
    """

    def setUp(self):
        """
        Set up test fixtures.
        """
        self.banking_system = BankingSystem()

    @patch("builtins.print")
    def test_authenticate_success(self, mock_print):
        """
        Test successful authentication.
        """
        # Call the authentication method
        result = self.banking_system.authenticate("user123", "pass123")

        # Assert authentication was successful
        self.assertTrue(result)
        mock_print.assert_called_once_with("User user123 authenticated successfully.")
        self.assertIn("user123", self.banking_system.logged_in_users)

    @patch("builtins.print")
    def test_authenticate_failure_wrong_password(self, mock_print):
        """
        Test authentication failure with wrong password.
        """
        # Call the authentication method with wrong password
        result = self.banking_system.authenticate("user123", "wrongpass")

        # Assert authentication failed
        self.assertFalse(result)
        mock_print.assert_called_once_with("Authentication failed.")
        self.assertNotIn("user123", self.banking_system.logged_in_users)

    @patch("builtins.print")
    def test_authenticate_failure_user_not_found(self, mock_print):
        """
        Test authentication failure with non-existent user.
        """
        # Call the authentication method with non-existent user
        result = self.banking_system.authenticate("panfilo", "pass123")

        # Assert authentication failed
        self.assertFalse(result)
        mock_print.assert_called_once_with("Authentication failed.")

    @patch("builtins.print")
    def test_authenticate_already_logged_in(self, mock_print):
        """
        Test authentication when user is already logged in.
        """
        # First login
        self.banking_system.authenticate("user123", "pass123")
        mock_print.reset_mock()  # Erase previous actions to reset the state of the mock

        # Try to login again
        result = self.banking_system.authenticate(
            "user123", "pass123"
        )  # Tries to authenticate a previously authenticated user

        # Assert that function returns False and prints appropriate message
        self.assertFalse(result)
        mock_print.assert_called_once_with("User already logged in.")

    @patch("white_box.class_exercises.BankAccount")
    @patch("builtins.print")
    def test_transfer_money_success_regular(self, mock_print, mock_bank_account):
        """
        Test successful regular money transfer.
        """
        # Authenticate user first
        self.banking_system.authenticate("user123", "pass123")

        # Mock the BankAccount instance and balance
        mock_account_instance = MagicMock()
        mock_account_instance.balance = 1000
        mock_bank_account.return_value = mock_account_instance

        # Call transfer_money
        result = self.banking_system.transfer_money(
            "user123", "user456", 100, "regular"
        )

        # Assert transfer was successful
        self.assertTrue(result)
        mock_print.assert_called_with(
            "Money transfer of $100 (regular transfer) from user123 to user456 "
            "processed successfully."
        )

    @patch("white_box.class_exercises.BankAccount")
    @patch("builtins.print")
    def test_transfer_money_success_express(self, mock_print, mock_bank_account):
        """
        Test successful express money transfer.
        """
        # Authenticate user first
        self.banking_system.authenticate("user123", "pass123")

        # Mock the BankAccount instance and balance
        mock_account_instance = (
            MagicMock()
        )  # Create a mock instance of BankAccount with MagicMock
        mock_account_instance.balance = 2000
        mock_bank_account.return_value = mock_account_instance

        # Call transfer_money
        result = self.banking_system.transfer_money(
            "user123", "user456", 500, "express"
        )

        # Assert transfer was successful
        self.assertTrue(result)
        mock_print.assert_called_with(
            "Money transfer of $500 (express transfer) from user123 to user456 "
            "processed successfully."
        )

    @patch("white_box.class_exercises.BankAccount")
    @patch("builtins.print")
    def test_transfer_money_success_scheduled(self, mock_print, mock_bank_account):
        """
        Test successful scheduled money transfer.
        """
        # Authenticate user first
        self.banking_system.authenticate("user123", "pass123")

        # Mock the BankAccount instance and balance
        mock_account_instance = (
            MagicMock()
        )  # Create a mock instance of BankAccount with MagicMock
        mock_account_instance.balance = 1500
        mock_bank_account.return_value = mock_account_instance

        # Call transfer_money
        result = self.banking_system.transfer_money(
            "user123", "user456", 200, "scheduled"
        )

        # Assert transfer was successful
        self.assertTrue(result)
        mock_print.assert_called_with(
            "Money transfer of $200 (scheduled transfer) from user123 to user456 "
            "processed successfully."
        )

    @patch("builtins.print")
    def test_transfer_money_sender_not_authenticated(self, mock_print):
        """
        Test transfer fails when sender is not authenticated.
        """
        # Call transfer_money without authenticating
        result = self.banking_system.transfer_money(
            "user123", "user456", 100, "regular"
        )

        # Assert transfer failed
        self.assertFalse(result)
        mock_print.assert_called_once_with("Sender not authenticated.")

    @patch("white_box.class_exercises.BankAccount")
    @patch("builtins.print")
    def test_transfer_money_insufficient_funds(self, mock_print, mock_bank_account):
        """
        Test transfer fails with insufficient funds.
        """
        # Authenticate user first
        self.banking_system.authenticate("user123", "pass123")

        # Mock the BankAccount instance with low balance
        mock_account_instance = MagicMock()
        mock_account_instance.balance = 50  # Not enough for 2000 plus the fee
        mock_bank_account.return_value = mock_account_instance

        # Call transfer_money
        result = self.banking_system.transfer_money(
            "user123", "user456", 2000, "regular"
        )

        # Assert transfer failed
        self.assertFalse(result)
        # Check that "Insufficient funds." was printed
        print_calls = [str(call) for call in mock_print.call_args_list]
        self.assertTrue(any("Insufficient funds." in call for call in print_calls))

    @patch("builtins.print")
    def test_transfer_money_invalid_transaction_type(self, mock_print):
        """
        Test transfer fails with invalid transaction type.
        """
        # Authenticate user first
        self.banking_system.authenticate("user123", "pass123")

        # Call transfer_money with invalid type
        result = self.banking_system.transfer_money(
            "user123", "user456", 100, "invalid_type"
        )  # Invented type

        # Assert transfer failed
        self.assertFalse(result)
        # Check that "Invalid transaction type." was printed
        print_calls = [str(call) for call in mock_print.call_args_list]
        self.assertTrue(
            any("Invalid transaction type." in call for call in print_calls)
        )


# 28
