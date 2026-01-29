from calculatorabs.calc_abstract import Calculator
from .fun_except import CustomException
import numbers

class CalculatorImp(Calculator):
    def add(self, a:float, b:float )-> float:
        if isinstance(a,numbers.Number) and isinstance(b,numbers.Number): # check to make sure input is numeric
            result = a + b
        else:
            raise CustomException("One or more entries were not numeric")
        return result
    
    def rounding(self, result:float)-> float:
        if isinstance(result,numbers.Number):
            return round(result)
        else:
            raise(CustomException("Could not round the value"))
    
    def subtract(self, a:float, b:float )-> float:
        if isinstance(a,numbers.Number) and isinstance(b,numbers.Number): # check to make sure input is numeric
            result = a-b
            return result
        else:
            raise CustomException("One or more entries were not numeric")
    
calc = CalculatorImp()
print(calc.add(5,5))