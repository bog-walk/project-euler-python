import unittest
from time import perf_counter
from solution.batch5.problem48 import self_powers_sum_brute, \
    self_powers_sum_modulo, self_powers_sum_modulo_2


class SelfPowers(unittest.TestCase):
    def test_self_powers_sum_low(self):
        nums = [1, 2, 3, 4, 6, 10]
        expected = [1, 5, 32, 288, 50069, 405071317]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], self_powers_sum_brute(n))
            self.assertEqual(expected[i], self_powers_sum_modulo(n))

    def test_self_powers_sum_mid(self):
        nums = [99, 1000, 8431]
        expected = [9027641920, 9110846700, 2756754292]
        for i, n in enumerate(nums):
            self.assertEqual(expected[i], self_powers_sum_brute(n))
            self.assertEqual(expected[i], self_powers_sum_modulo(n))

    def test_self_powers_sum_speed(self):
        n = 10_000
        expected = 6237204500
        brute_start = perf_counter()
        self.assertEqual(expected, self_powers_sum_brute(n))
        brute_stop = perf_counter()
        mod_start = perf_counter()
        self.assertEqual(expected, self_powers_sum_modulo(n))
        mod_stop = perf_counter()
        mod_start_2 = perf_counter()
        self.assertEqual(expected, self_powers_sum_modulo_2(n))
        mod_stop_2 = perf_counter()
        print(f"Brute solution took: {brute_stop - brute_start:0.2f}s\n" +
              f"Mod solution took: {mod_stop - mod_start:0.2f}s\n" +
              f"Mod_2 solution took: {mod_stop_2 - mod_start_2:0.2f}s\n")


if __name__ == '__main__':
    unittest.main()
