"""
This module provides functions to convert between pounds and pence.

Functions:
    pence(pounds): Converts pounds to pence.
    pounds(pence): Converts pence to pounds and formats the result to two decimal places.

Exceptions:
    TypeError: Raised when the input is not an integer or float.
    ValueError: Raised when the input is a negative number.
"""


def pence(pounds):
    """
    This function converts pounds to pence.

    Args:
        pounds (int or float): The amount in pounds to be converted.

    Returns:
        int: The equivalent amount in pence.

    Raises:
        TypeError: If the input is not an integer or float.
        ValueError: If the input is a negative number.
    """
    if not isinstance(pounds, (int, float)):
        raise TypeError("Input must be an integer or float.")
    if pounds < 0:
        raise ValueError("Input must be a non-negative number.")

    return int(pounds * 100)


def pounds(pence):
    """
    This function converts pence to pounds and formats the result to two decimal places.

    Args:
        pence (int or float): The amount in pence to be converted to pounds.

    Returns:
        str: The converted amount in pounds, formatted to two decimal places.

    Raises:
        TypeError: If the input is not a number.
        ValueError: If the pence value is negative.
    """
    if not isinstance(pence, (int, float)):
        raise TypeError("Input must be an integer or float")

    # Handle negative values
    if pence < 0:
        raise ValueError("Pence value cannot be negative")

    return f"{pence / 100:.2f}"
