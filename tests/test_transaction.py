import pytest

from src.transaction import Transaction


# Test cases for the Transaction class
class TestTransaction:
    def test_init_valid_data(self):
        """
        Test that a new Transaction instance is correctly initialized with valid data.
        """
        transaction = Transaction(credit=100, debit=50, balance=450)
        assert transaction.credit == 100
        assert transaction.debit == 50
        assert transaction.balance == 450

    def test_init_invalid_credit_type(self):
        """
        Test that a TypeError is raised when the credit amount is not a number.
        """
        with pytest.raises(TypeError):
            Transaction(credit="not_a_number")

    def test_init_invalid_credit_value(self):
        """
        Test that a ValueError is raised when the credit amount is negative.
        """
        with pytest.raises(ValueError):
            Transaction(credit=-100)

    def test_init_invalid_debit_type(self):
        """
        Test that a TypeError is raised when the debit amount is not a number.
        """
        with pytest.raises(TypeError):
            Transaction(debit="not_a_number")

    def test_init_invalid_debit_value(self):
        """
        Test that a ValueError is raised when the debit amount is negative.
        """
        with pytest.raises(ValueError):
            Transaction(debit=-100)

    def test_init_invalid_balance_type(self):
        """
        Test that a TypeError is raised when the balance is not a number.
        """
        with pytest.raises(TypeError):
            Transaction(balance="not_a_number")
