import pytest
from app.calculator import Calculator

class TestCalculator:

    def setup(self):
        self.calc = Calculator

    def teardown(self):
        print('Teardown')

    # проверяем функцию сложения
    def test_adding_success(self):
        assert self.calc.adding(self, 2, 3) == 5

    # проверяем функцию умножения
    def test_multiplying_success(self):
        assert self.calc.multiply(self, 2, 3) == 6

    # проверяем функцию деления
    def test_divisioning_success(self):
        assert self.calc.division(self, 6, 3) == 2

    # проверяем функцию вычитания
    def test_subtractioning_success(self):
        assert self.calc.subtraction(self, 6, 3) == 3

    # проверяем работу исключения при делении на ноль
    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)