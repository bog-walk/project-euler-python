import unittest
from solution.batch1.problem2 import *


class EvenFibonacciNumbers(unittest.TestCase):
    def test_max_is_even_fibonacci(self):
        self.assertEqual(3382, even_fibonacci_step(10946))
        self.assertEqual(3382, even_fibonacci_formula(10946))

    def test_max_is_odd(self):
        self.assertEqual(798, even_fibonacci_step(2583))
        self.assertEqual(798, even_fibonacci_formula(2583))

    def test_normal_n(self):
        self.assertEqual(188, even_fibonacci_step(200))
        self.assertEqual(188, even_fibonacci_formula(200))

    def test_large_n(self):
        self.assertEqual(4613732, even_fibonacci_step(4000000))
        self.assertEqual(4613732, even_fibonacci_formula(4000000))

    def test_lower_limits(self):
        self.assertEqual(10, even_fibonacci_step(10))
        self.assertEqual(10, even_fibonacci_formula(10))

    def test_upper_limits(self):
        self.assertEqual(49597426547377748, even_fibonacci_step(40000000000000000))
        self.assertEqual(49597426547377748, even_fibonacci_formula(40000000000000000))


if __name__ == '__main__':
    unittest.main()
