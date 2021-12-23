import unittest
from time import perf_counter
from solution.batch5.problem43 import sum_of_pandigital_substrings, \
    sum_of_9_pandigital_substrings


class SubstringDivisibility(unittest.TestCase):
    def test_sum_of_pandigital_subs(self):
        expected = [
            22212, 711104, 12444480, 189838560, 1099210170, 1113342912, 16695334890
        ]
        for n in range(3, 10):
            self.assertEqual(expected[n-3], sum_of_pandigital_substrings(n))

    def test_sum_of_9_pandigital_subs_speed(self):
        expected = 16695334890
        brute_start = perf_counter()
        self.assertEqual(expected, sum_of_pandigital_substrings(9))
        brute_stop = perf_counter()
        filtered_start = perf_counter()
        self.assertEqual(expected, sum_of_9_pandigital_substrings())
        filtered_stop = perf_counter()
        print(f"Brute solution took: {brute_stop - brute_start:0.4f}s\n"
              f"Filtered solution took: {filtered_stop - filtered_start:0.4f}s\n")


if __name__ == '__main__':
    unittest.main()
