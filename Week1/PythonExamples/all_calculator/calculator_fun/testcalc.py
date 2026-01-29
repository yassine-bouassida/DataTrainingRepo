from calculator_implemented import CalculatorImp

calculator = CalculatorImp()

def test_addition_success():
    result = calculator.add(5,5)
    assert result == 10 #we expect 5+5 to equal 10
