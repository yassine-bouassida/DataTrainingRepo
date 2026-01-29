from abc import ABC, abstractmethod
class Calculator(ABC):
    @abstractmethod
    def add(self, a: float, b: float) -> float:
        pass

    @abstractmethod
    def subtract(self, a: float, b: float) -> float:
        pass

    @abstractmethod
    def rounding(self, result: float) -> int:
        pass