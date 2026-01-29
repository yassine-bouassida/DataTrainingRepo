from interface import Calculator

class CalculatorImp(Calculator):
    def add(self, a:float, b:float )-> float:
        result = a + b
        return result
    
calc = CalculatorImp()
print(calc.add(5,5))