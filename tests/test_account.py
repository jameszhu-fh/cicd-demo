import pytest

from src.account import Account, Printer, Transaction


# Mock classes for testing
class MockTransaction(Transaction):
    def display(self):
        return "Mock Transaction"


class MockPrinter(Printer):
    def print_statement(self, rows):
        pass  # In real test, you could accumulate the rows for later assertions


# Fixture for creating a test account
@pytest.fixture
def account():
    return Account(transaction_class=MockTransaction, printer_class=MockPrinter)


# Test cases
def test_deposit_valid_amount(account):
    assert "deposited" in account.deposit(100)


def test_deposit_invalid_amount(account):
    assert "Invalid amount" in account.deposit(-1)


def test_withdraw_valid_amount(account):
    account.deposit(200)  # Make sure there is enough balance
    assert "withdrawn" in account.withdraw(50)


def test_withdraw_invalid_amount(account):
    assert "Invalid amount" in account.withdraw(-1)


def test_withdraw_insufficient_funds(account):
    assert "Insufficient funds" in account.withdraw(100)


def test_statement(account):
    account.deposit(100)
    account.statement()  # This should not raise an error if it's correctly mocked
