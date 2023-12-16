import unittest
from app.calculator import Calculator

class TestCalculatorMethods(unittest.TestCase):
    def setUp(self):
        # Ініціалізація об'єкту Calculator для кожного тесту
        self.calc = Calculator(5, 2)

    def test_add(self):
        self.assertEqual(self.calc.add(), 7)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(), 3)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(), 10)

    def test_divide(self):
        self.assertEqual(self.calc.divide(), 2.5)
        # Тест на ділення на нуль
        calc_divide_by_zero = Calculator(5, 0)
        self.assertEqual(calc_divide_by_zero.divide(), "Error: Division by zero")

    def test_power(self):
        self.assertEqual(self.calc.power(), 25.0)