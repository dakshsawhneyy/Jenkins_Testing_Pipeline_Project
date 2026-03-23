# Import unittest module and app module
import unittest
import app


# Import unit function
class TestCalculator(unittest.TestCase):

    def test_add(self):
        result = app.add(2, 3)
        self.assertEqual(result, 5)

    def test_subtract(self):
        result = app.subtract(5, 3)
        self.assertEqual(result, 2)

    def test_multiply(self):
        result = app.multiply(2, 3)
        self.assertEqual(result, 6)

    def test_divide(self):
        result = app.divide(6, 2)
        self.assertEqual(result, 3)

    # Exceptional Test Case
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            app.divide(2, 0)


# Main Function
if __name__ == "__main__":
    unittest.main()
