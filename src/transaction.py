"""
This module contains the Transaction class which represents a single transaction in the bank account.

The Transaction class has three attributes: credit, debit, and balance.

The class also has a method called display() which returns a string representation of the transaction.

The class uses the money module to convert the credit and debit amounts to pounds and pence.

Note: This module depends on the money module for currency conversion and formatting.
"""

import datetime

from .money import pounds


class Transaction:
    """
    A class representing a single transaction in the bank account.
    """

    def __init__(self, credit=None, debit=None, balance=None):
        """
        Initializes a new instance of the Transaction class.

        Parameters:
        credit (float): The credit amount for the transaction. Must be a non-negative number.
        debit (float): The debit amount for the transaction. Must be a non-negative number.
        balance (float): The account balance after the transaction. Must be a number.

        Raises:
        TypeError: If any of the parameters is not a number.
        ValueError: If credit or debit is a negative number.
        """
        if credit is not None:
            if not isinstance(credit, (int, float)):
                raise TypeError("Credit must be a number")
            if credit < 0:
                raise ValueError("Credit must be a non-negative number")
        if debit is not None:
            if not isinstance(debit, (int, float)):
                raise TypeError("Debit must be a number")
            if debit < 0:
                raise ValueError("Debit must be a non-negative number")
        if balance is not None and not isinstance(balance, (int, float)):
            raise TypeError("Balance must be a number")

        self.date = datetime.datetime.now()
        self.date_format = self.date.strftime("%d/%m/%Y")
        self.credit = credit
        self.debit = debit
        self.balance = balance

    def display(self):
        """
        Returns a string representation of the transaction.

        Returns:
        str: A string representing the transaction, including the date, credit, debit, and balance.
        """
        separator = "|| "
        items = [
            self.date_format,
            self.__render(self.credit),
            self.__render(self.debit),
            self.__render(self.balance),
        ]
        return separator.join(items).strip()

    def __render(self, item):
        """
        Converts the given item to a string in pounds and pence format.

        Parameters:
        item (float): The item to be rendered.

        Returns:
        str: A string representing the item in pounds and pence format.
        """
        if item is not None:
            try:
                template = "{}"
                return template.format(pounds(item))
            except Exception as e:
                return f"Error: {e}"
        return ""
