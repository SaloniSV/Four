import unittest
import Calcul

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calcul.add(2, 5), 7)


    def test_add(self):
        self.assertNotEqual(Calcul.add(10,14), 7)

    def test_multiply(self):
        self.assertEqual(Calcul.multiply(2, 10), 20)


    def test_multiply(self):
        self.assertEqual(Calcul.multiply(5,8), 40 )

    def test_subtract(self):
        self.assertEqual(Calcul.subtract(240, 150), 90)


    def test_divide(self):
        self.asserEqual(Calcul.divide(100,10), 10)

    def test_divide(self):
        self.assertEqual(Calcul.divide(150, 5), 10)


    def test_subtract(self):
        self.assertEqual(Calcul.subtract(79,19), 60)
