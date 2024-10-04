import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # Test for addition
    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -7), -12)
        self.assertEqual(self.calc.add(0, 0), 0)

    # Test for subtraction
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(3, 5), -2)

    # Test for multiplication
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(-4, -2), 8)

    # Test for division
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertEqual(self.calc.divide(-9, -3), 3)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        
        # Test division by zero
        self.assertIsNone(self.calc.divide(10, 0), "Division by zero should return None")
    
    # Edge case: large numbers
    def test_large_numbers(self):
        self.assertEqual(self.calc.add(1e12, 1e12), 2e12)
        self.assertEqual(self.calc.subtract(1e12, 1e6), 1e12 - 1e6)
        self.assertEqual(self.calc.multiply(1e6, 1e6), 1e12)
        self.assertEqual(self.calc.divide(1e12, 1e6), 1e6)

if __name__ == "__main__":
    unittest.main()
