import unittest
from solution.batch8.problem88 import sum_of_ps_numbers, generate_ps_numbers


class ProductSumNumbers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        generate_ps_numbers()

    def test_lower_constraints(self):
        expected = [4, 10, 18, 18, 30]
        for k in range(2, 7):
            self.assertEqual(expected[k-2], sum_of_ps_numbers(k))

    def test_lower_mid_constraints(self):
        inputs = [12, 15, 27, 53, 100, 500]
        expected = [61, 123, 288, 684, 2061, 29836]
        for k, e in zip(inputs, expected):
            self.assertEqual(e, sum_of_ps_numbers(k))

    def test_upper_mid_constraints(self):
        inputs = [1000, 5000, 12000]
        expected = [93063, 1_517_617, 7_587_457]
        for k, e in zip(inputs, expected):
            self.assertEqual(e, sum_of_ps_numbers(k))

    def test_upper_constraints(self):
        inputs = [60_000, 100_000, 200_000]
        expected = [135_517_061, 344_017_453, 1_229_547_946]
        for k, e in zip(inputs, expected):
            self.assertEqual(e, sum_of_ps_numbers(k))


if __name__ == '__main__':
    unittest.main()
