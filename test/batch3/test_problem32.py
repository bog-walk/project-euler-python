import unittest
from util.tests.reusable import compare_speed
from solution.batch3.problem32 import sum_pandigital_products_brute, \
    sum_pandigital_products


class PandigitalProducts(unittest.TestCase):
    def test_all_but_upper(self):
        expected = [12, 52, 162, 0, 13458]
        for n in range(4, 9):
            self.assertEqual(expected[n - 4], sum_pandigital_products_brute(n))
            self.assertEqual(expected[n - 4], sum_pandigital_products(n))

    def test_sum_pandigital_products_speed(self):
        n = 9
        expected = 45228
        solutions = {
            "Brute": [sum_pandigital_products_brute, n],
            "Built-in": [sum_pandigital_products, n]
        }
        results = compare_speed(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
