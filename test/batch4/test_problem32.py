import unittest
from solution.batch4.problem32 import sum_pandigital_products


class PandigitalProducts(unittest.TestCase):
    def test_sum_pandigital_products(self):
        expected = [12, 52, 162, 0, 13458, 45228]
        for n in range(4, 10):
            self.assertEqual(expected[n - 4], sum_pandigital_products(n))


if __name__ == '__main__':
    unittest.main()
