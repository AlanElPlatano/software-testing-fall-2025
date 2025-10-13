# -*- coding: utf-8 -*-
"""
Mock up testing examples for BankingSystem.
"""
import unittest
from unittest.mock import MagicMock, patch

from white_box.class_exercises import BankAccount, BankingSystem, Product, ShoppingCart


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
class TestProduct(unittest.TestCase):
    """
    Product unittest class.
    """

    @patch("builtins.print")
    def test_view_product(self, mock_print):
        """
        Test view_product displays correct information.
        """
        # Create a product instance
        product = Product("Laptop", 999.99)

        # Call the method under test
        result = product.view_product()

        # Assert return value is correct
        self.assertEqual(result, "The product Laptop has a price of 999.99")
        # Assert print was called with the expected message
        mock_print.assert_called_once_with("The product Laptop has a price of 999.99")


class TestShoppingCart(unittest.TestCase):
    """
    ShoppingCart unittest class.
    """

    def setUp(self):
        """
        Set up test fixtures.
        """
        self.cart = ShoppingCart()
        self.product1 = Product("Laptop", 999.99)
        self.product2 = Product("Mouse", 25.50)
        self.product3 = Product("Keyboard", 75.00)

    def test_add_product_single(self):
        """
        Test adding a single product to the cart.
        """
        # Add product to cart
        self.cart.add_product(self.product1)

        # Assert cart contains the product
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["product"], self.product1)
        self.assertEqual(self.cart.items[0]["quantity"], 1)

    def test_add_product_with_quantity(self):
        """
        Test adding a product with specific quantity.
        """
        # Add product with quantity 3
        self.cart.add_product(self.product2, 3)

        # Assert cart contains the product with correct quantity
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["product"], self.product2)
        self.assertEqual(self.cart.items[0]["quantity"], 3)

    def test_add_product_multiple_times(self):
        """
        Test adding the same product multiple times increases quantity.
        """
        # Add product twice
        self.cart.add_product(self.product1, 2)
        self.cart.add_product(self.product1, 3)

        # Assert cart contains only one entry with combined quantity
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["product"], self.product1)
        self.assertEqual(self.cart.items[0]["quantity"], 5)

    def test_add_multiple_different_products(self):
        """
        Test adding multiple different products to the cart.
        """
        # Add different products
        self.cart.add_product(self.product1)
        self.cart.add_product(self.product2, 2)
        self.cart.add_product(self.product3)

        # Assert cart contains all products
        self.assertEqual(len(self.cart.items), 3)

    def test_remove_product_partial(self):
        """
        Test removing partial quantity of a product.
        """
        # Add product with quantity 5
        self.cart.add_product(self.product1, 5)

        # Remove 2 items
        self.cart.remove_product(self.product1, 2)

        # Assert product still in cart with reduced quantity
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["quantity"], 3)

    def test_remove_product_completely(self):
        """
        Test removing all quantity of a product removes it from cart.
        """
        # Add product with quantity 3
        self.cart.add_product(self.product2, 3)

        # Remove 3 items (all of them)
        self.cart.remove_product(self.product2, 3)

        # Assert cart is empty
        self.assertEqual(len(self.cart.items), 0)

    def test_remove_product_more_than_available(self):
        """
        Test removing more quantity than available removes product completely.
        """
        # Add product with quantity 2
        self.cart.add_product(self.product3, 2)

        # Try to remove 5 items (more than available)
        self.cart.remove_product(self.product3, 5)

        # Assert cart is empty
        self.assertEqual(len(self.cart.items), 0)

    def test_remove_product_not_in_cart(self):
        """
        Test removing a product that is not in the cart.
        """
        # Add one product
        self.cart.add_product(self.product1)

        # Try to remove a different product
        self.cart.remove_product(self.product2)

        # Assert cart still contains original product
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["product"], self.product1)

    @patch("builtins.print")
    def test_view_cart_single_product(self, mock_print):
        """
        Test viewing cart with a single product.
        """
        # Add product to cart
        self.cart.add_product(self.product1, 2)

        # View cart
        self.cart.view_cart()

        # Assert print was called with correct information
        mock_print.assert_called_once_with("2 x Laptop - $1999.98")

    @patch("builtins.print")
    def test_view_cart_multiple_products(self, mock_print):
        """
        Test viewing cart with multiple products.
        """
        # Add products to cart
        self.cart.add_product(self.product1, 1)
        self.cart.add_product(self.product2, 3)
        self.cart.add_product(self.product3, 2)

        # View cart
        self.cart.view_cart()

        # Assert print was called for each product
        self.assertEqual(mock_print.call_count, 3)
        calls = [str(call) for call in mock_print.call_args_list]
        self.assertTrue(any("1 x Laptop - $999.99" in call for call in calls))
        self.assertTrue(any("3 x Mouse - $76.5" in call for call in calls))
        self.assertTrue(any("2 x Keyboard - $150.0" in call for call in calls))

    @patch("builtins.print")
    def test_view_cart_empty(self, mock_print):
        """
        Test viewing an empty cart.
        """
        # View empty cart
        self.cart.view_cart()

        # Assert print was not called
        mock_print.assert_not_called()

    @patch("builtins.print")
    def test_checkout_single_product(self, mock_print):
        """
        Test checkout with a single product.
        """
        # Add product to cart
        self.cart.add_product(self.product1, 1)

        # Checkout
        self.cart.checkout()

        # Assert print was called with total and completion message
        self.assertEqual(mock_print.call_count, 2)
        mock_print.assert_any_call("Total: $999.99")
        mock_print.assert_any_call("Checkout completed. Thank you for shopping!")

    @patch("builtins.print")
    def test_checkout_multiple_products(self, mock_print):
        """
        Test checkout with multiple products.
        """
        # Add products to cart
        self.cart.add_product(self.product1, 2)  # 2 * 999.99 = 1999.98
        self.cart.add_product(self.product2, 3)  # 3 * 25.50 = 76.50
        self.cart.add_product(self.product3, 1)  # 1 * 75.00 = 75.00

        # Checkout
        self.cart.checkout()

        # Assert print was called with correct total
        self.assertEqual(mock_print.call_count, 2)
        mock_print.assert_any_call("Total: $2151.48")
        mock_print.assert_any_call("Checkout completed. Thank you for shopping!")

    @patch("builtins.print")
    def test_checkout_empty_cart(self, mock_print):
        """
        Test checkout with an empty cart.
        """
        # Checkout empty cart
        self.cart.checkout()

        # Assert print was called with zero total
        self.assertEqual(mock_print.call_count, 2)
        mock_print.assert_any_call("Total: $0")
        mock_print.assert_any_call("Checkout completed. Thank you for shopping!")

    def test_cart_workflow(self):
        """
        Test complete shopping workflow: add, remove, and verify.
        """
        # Add products
        self.cart.add_product(self.product1, 2)
        self.cart.add_product(self.product2, 5)
        self.cart.add_product(self.product3, 1)

        # Remove some items
        self.cart.remove_product(self.product2, 2)  # Reduce mouse quantity
        self.cart.remove_product(self.product3, 1)  # Remove keyboard completely

        # Verify cart state
        self.assertEqual(len(self.cart.items), 2)
        # Check laptop quantity
        laptop_item = next(
            item for item in self.cart.items if item["product"] == self.product1
        )
        self.assertEqual(laptop_item["quantity"], 2)
        # Check mouse quantity
        mouse_item = next(
            item for item in self.cart.items if item["product"] == self.product2
        )
        self.assertEqual(mouse_item["quantity"], 3)
