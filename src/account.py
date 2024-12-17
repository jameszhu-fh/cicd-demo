"""
This module defines the Account class, which manages the bank account operations.
It includes methods for deposit, withdrawal, and printing the account statement.

Classes:
- Account: Manages the bank account operations.

Functions:
- deposit: Processes the deposit operation for the account.
- withdraw: Withdraws a specified amount from the account.
- statement: Generates and prints the account statement.

Note: This module depends on the money module for currency conversion and formatting.
"""

from . import money
from .printer import Printer
from .transaction import Transaction


class Account:
    """
    Account class for managing bank account operations.
    """

    def __init__(self, transaction_class=Transaction, printer_class=Printer):
        """
        Initialize the account class.

        This class is used to manage account balance, transaction history, and print output.
        During initialization, custom transaction and printer classes can be passed in to achieve different behaviors.

        Parameters:
        - transaction_class: Transaction class, default is Transaction. Used to create transaction objects.
        - printer_class: Printer class, default is Printer. Used to create print output objects.

        Returns:
        None.
        """
        if not issubclass(transaction_class, Transaction):
            raise TypeError("transaction_class must be a subclass of Transaction")
        if not issubclass(printer_class, Printer):
            raise TypeError("printer_class must be a subclass of Printer")

        self.balance = 0
        self.transaction_class = transaction_class
        self.transaction_history = []
        self.printer = printer_class()

    def deposit(self, amount):
        """
        Processes the deposit operation for the account.

        Converts the deposited amount into the smallest currency unit (pence) to ensure transaction accuracy.
        Updates the account balance and records the transaction detail.
        Returns the deposit message and the updated balance.

        Parameters:
        amount (int): The amount to be deposited, in the basic currency unit.

        Returns:
        str: The deposit confirmation message and the updated balance.
        """
        try:
            credit = money.pence(amount)
        except ValueError as e:
            return f"Invalid amount: {e}"

        self.balance += credit
        self.__add_transaction(credit=credit, balance=self.balance)
        message = "{0} deposited. Current balance: {1}"
        return message.format(money.pounds(credit), money.pounds(self.balance))

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account.

        This method first converts the input amount to pence to ensure accurate calculations.
        If the withdrawal amount exceeds the account balance, it returns the message "Insufficient funds".
        Otherwise, it updates the account balance and records the transaction details.
        Finally, it returns a message indicating the amount withdrawn and the current balance.

        Parameters:
        amount (float): The amount to be withdrawn, in pounds.

        Returns:
        str: A message containing the transaction result and the current balance.
        """
        if amount <= 0:
            return "Invalid amount"

        try:
            debit = money.pence(amount)
        except ValueError as e:
            return f"Invalid amount: {e}"

        if debit > self.balance:
            return "Insufficient funds"

        self.balance -= debit
        self.__add_transaction(debit=debit, balance=self.balance)
        message = "{0} withdrawn. Current balance: {1}"
        return message.format(money.pounds(debit), money.pounds(self.balance))

    def statement(self):
        """
        Generate and print the account statement.

        This method reverses the transaction history to display the most recent transactions first,
        maps each transaction to its display format, and prints the statement using the printer object.
        """
        mapped_rows = map(
            self.__transaction_mapping, reversed(self.transaction_history)
        )
        self.printer.print_statement(mapped_rows)

    def __add_transaction(self, credit=None, debit=None, balance=None):
        """
        Add a transaction to the transaction history.

        Creates a new transaction object using the provided credit, debit, and balance,
        and appends it to the transaction history list.

        Parameters:
        - credit (int): The amount credited to the account, in pence.
        - debit (int): The amount debited from the account, in pence.
        - balance (int): The account balance after the transaction, in pence.

        Returns:
        None.
        """
        transaction = self.transaction_class(credit, debit, balance)
        self.transaction_history.append(transaction)

    def __transaction_mapping(self, transaction):
        """
        Map a transaction to its display format.

        Calls the display method of the transaction object to get its formatted string representation.

        Parameters:
        transaction (Transaction): The transaction object to be mapped.

        Returns:
        str: The formatted string representation of the transaction.
        """
        return transaction.display()
