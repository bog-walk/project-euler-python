import unittest
from util.tests.reusable import compare_speed
from solution.batch6.problem69 import max_totient_ratio, max_totient_ratio_primorial


class TotientMaximum(unittest.TestCase):
    def test_lower_constraints(self):
        nums = [3, 5, 10, 15, 20, 25, 31]
        expected = [2, 2, 6, 6, 6, 6, 30]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], max_totient_ratio(n))
            self.assertEqual(expected[i], max_totient_ratio_primorial(n))

    def test_mid_constraints(self):
        nums = [100, 200, 399, 450, 1000, 6000, 100_000]
        expected = [30, 30, 210, 210, 210, 2310, 30030]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], max_totient_ratio(n))
            self.assertEqual(expected[i], max_totient_ratio_primorial(n))

    def test_primorial_correct_for_upper_constraints(self):
        expected = [
            223_092_870, 200_560_490_130, 304_250_263_527_210,
            614_889_782_588_491_410
        ]
        for i, e in enumerate(range(9, 19, 3)):
            n = pow(10, e)
            self.assertEqual(expected[i], max_totient_ratio_primorial(n))

    def test_primorial_correct_when_limit_is_max_n(self):
        limit = 614_889_782_588_491_410  # max n less than N = 1e18
        expected = 13_082_761_331_670_030
        self.assertEqual(expected, max_totient_ratio_primorial(limit))

    def test_max_totient_ratio_speed(self):
        limit = 1_000_000
        expected = 510_510
        solutions = {
            "Totient": [max_totient_ratio, limit],
            "Primorial": [max_totient_ratio_primorial, limit]
        }
        results = compare_speed(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
