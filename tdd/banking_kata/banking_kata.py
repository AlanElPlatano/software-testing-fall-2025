"""
Banking Kata

Implements a simple bank account with deposit, withdrawal, and statement printing.
"""

from datetime import datetime
from typing import Dict, List


class Account:
    """
    Represents a simple bank account.
    Only the methods defined here are public:
    - deposit(amount)
    - withdraw(amount)
    - print_statement()
    """

    def __init__(self, printer):
        self.transactions: List[Dict[str, int | str]] = []
        self.balance = 0
        self.printer = printer  # injected dependency for testability

    def deposit(self, amount: int, date: str = None):
        """Deposit an amount into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        date = date or self._today()
        self.transactions.append(
            {"date": date, "amount": amount, "balance": self.balance}
        )

    def withdraw(self, amount: int, date: str = None):
        """Withdraw an amount from the account."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        self.balance -= amount
        date = date or self._today()
        self.transactions.append(
            {"date": date, "amount": -amount, "balance": self.balance}
        )

    def print_statement(self):
        """Print the statement via the injected printer."""
        self.printer.print_line("DATE | AMOUNT | BALANCE")
        # Reverse order: most recent transaction first
        for t in reversed(self.transactions):
            line = f"{t['date']} | {t['amount']:.2f} | {t['balance']:.2f}"
            self.printer.print_line(line)

    # --- Private helper ---
    def _today(self):
        """Return today's date as dd/mm/yyyy string"""
        return datetime.now().strftime("%d/%m/%Y")


class ConsolePrinter:
    """Responsible for printing lines to the console."""

    def print_line(self, line: str):
        """Print a single line to the console."""
        print(line)


if __name__ == "__main__":
    # Example usage
    printer = ConsolePrinter()
    account = Account(printer)
    account.deposit(1000, "01/04/2014")
    account.withdraw(100, "02/04/2014")
    account.deposit(500, "10/04/2014")
    account.print_statement()
