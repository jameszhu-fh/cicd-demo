"""
This module contains the printer class which is used to print the statement.
"""

ROW_SEPARATOR = "\n"


class Printer:
    """
    This class is used to print the statement.
    """

    statement_header = "date || credit || debit || balance \n"

    def print_statement(self, transactions):
        """
        Prints the statement.

        Args:
            transactions (list of str): A list of transaction rows to be printed.
        """

        if not transactions:
            print(self.statement_header + "No transactions to display.")
            return

        try:
            # 验证每一行是否为字符串
            for row in transactions:
                if not isinstance(row, str):
                    raise ValueError("Transaction rows must be strings")

            # 将交易行连接起来
            joined_transaction_rows = ROW_SEPARATOR.join(transactions)
            print(self.statement_header + joined_transaction_rows)
        except Exception as e:
            print(f"Error: {e}")
