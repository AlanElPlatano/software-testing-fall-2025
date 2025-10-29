"""
Data-driven and mock-based tests for the Banking Kata
"""

from unittest.mock import Mock, call

import pytest

from tdd.banking_kata.banking_kata import Account


class TestBankingKata:
    """Tests for deposit, withdrawal, and statement printing"""

    @pytest.fixture
    def printer(self):
        """Mock printer to capture printed output"""
        return Mock()

    @pytest.fixture
    def account(self, printer):
        """Creates a fresh account instance with mock printer"""
        return Account(printer)

    @pytest.mark.parametrize(
        "action,amount,date",
        [
            ("deposit", 1000, "01/04/2014"),
            ("withdraw", 100, "02/04/2014"),
            ("deposit", 500, "10/04/2014"),
        ],
    )
    def test_transactions_are_recorded_correctly(self, account, action, amount, date):
        """Ensure deposits and withdrawals affect balance correctly"""
        getattr(account, action)(amount, date)
        last_txn = account.transactions[-1]
        assert last_txn["amount"] == (amount if action == "deposit" else -amount)
        assert last_txn["date"] == date
        assert "balance" in last_txn

    def test_prints_statement_in_reverse_order(self, account, printer):
        """Ensure statement prints newest transaction first"""
        account.deposit(1000, "01/04/2014")
        account.withdraw(100, "02/04/2014")
        account.deposit(500, "10/04/2014")

        account.print_statement()

        # Validate calls
        printer.print_line.assert_any_call("DATE | AMOUNT | BALANCE")
        printer.print_line.assert_has_calls(
            [
                # Most recent first
                call("10/04/2014 | 500.00 | 1400.00"),
                call("02/04/2014 | -100.00 | 900.00"),
                call("01/04/2014 | 1000.00 | 1000.00"),
            ]
        )

    def test_negative_deposit_or_withdraw_raises_error(self, account):
        """Ensure negative deposits or withdrawals raise ValueError"""
        with pytest.raises(ValueError):
            account.deposit(0)
        with pytest.raises(ValueError):
            account.withdraw(-50)

    def test_empty_statement_prints_header_only(self, account, printer):
        """Ensure printing statement with no transactions only prints header"""
        account.print_statement()
        printer.print_line.assert_called_once_with("DATE | AMOUNT | BALANCE")
