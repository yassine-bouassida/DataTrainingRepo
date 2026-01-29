from calculatorpack.calculator_implemented import CalculatorImp
import pytest

from calculatorpack.fun_except import CustomException

calculator = CalculatorImp()

def test_addition_success():
    result = calculator.add(5,5)
    assert result == 10 #we expect 5+5 to equal 10

def test_round_success():
    result = calculator.rounding(1.1)
    assert result == 1

def test_subtration_success():
    result = calculator.subtract(5,5)
    assert result == 0 #we expect 5+5 to equal 10

def test_addition_strings_entered():
    with pytest.raises(CustomException):
        result = calculator.add("one","two")

def test_subtraction_strings_entered():
    with pytest.raises(CustomException):
        result = calculator.subtract("one","two")

def test_round_string_entered():
    with pytest.raises(CustomException):
        result = calculator.rounding("five point 1")

def test_addition_exception_message_correct():
    try:
        result = calculator.add(1,"1")
        assert False
    except CustomException as e:
        assert e.message == "One or more entries were not numeric"

def test_subtraction_exception_message_correct():
    try:
        result = calculator.subtract(1,"1")
        assert False
    except CustomException as e:
        assert e.message == "One or more entries were not numeric"

def test_round_exception_message_correct():
    try:
        result = calculator.rounding("1.1")
        assert False
    except CustomException as e:
        assert e.message == "Could not round the value"


# calculator = CalculatorImp()
# calculator.add(5,5)