import pytest

from src.money import pence, pounds


# Test cases for the pence function
def test_pence_with_int():
    assert pence(1) == 100


def test_pence_with_float():
    assert pence(1.5) == 150


def test_pence_with_negative_raises_value_error():
    with pytest.raises(ValueError):
        pence(-1)


def test_pence_with_non_number_raises_type_error():
    with pytest.raises(TypeError):
        pence("not a number")


# Test cases for the pounds function
def test_pounds_with_int():
    assert pounds(100) == "1.00"


def test_pounds_with_float():
    assert pounds(250) == "2.50"


def test_pounds_with_negative_raises_value_error():
    with pytest.raises(ValueError):
        pounds(-50)


def test_pounds_with_non_number_raises_type_error():
    with pytest.raises(TypeError):
        pounds("not a number")
