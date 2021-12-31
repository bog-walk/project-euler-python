import unittest
from time import perf_counter
from solution.batch5.problem50 import consecutive_prime_sum, \
    consecutive_prime_sum_improved


class ConsecutivePrimeSum(unittest.TestCase):
    def test_consecutive_prime_sum_low(self):
        nums = [
            2, 5, 10, 20, 50, 100, 150, 200, 300, 500, 1000, 2000, 10000, 22340
        ]
        expected = [
            (2, 1), (5, 2), (5, 2), (17, 4), (41, 6), (41, 6), (127, 9),
            (197, 12), (281, 14), (499, 17), (953, 21),
            (1583, 27), (9521, 65), (22039, 96)
        ]
        for i, n in enumerate(nums):
            self.assertTupleEqual(expected[i], consecutive_prime_sum(n))
            self.assertTupleEqual(expected[i], consecutive_prime_sum_improved(n))

    def test_consecutive_prime_sum_mid(self):
        expected = [
            (92951, 183), (997651, 543),
            (9951191, 1587), (99819619, 4685), (999715711, 13935)
        ]
        for i in range(5, 10):
            n = pow(10, i)
            self.assertTupleEqual(expected[i - 5], consecutive_prime_sum(n))
            self.assertTupleEqual(expected[i - 5], consecutive_prime_sum_improved(n))

    def test_consecutive_prime_sum_high(self):
        expected = [(99987684473, 125479), (999973156643, 379317)]
        for i in range(11, 13):
            n = pow(10, i)
            self.assertTupleEqual(expected[i - 11], consecutive_prime_sum_improved(n))

    def test_consecutive_prime_sum_speed(self):
        solutions = [
            consecutive_prime_sum, consecutive_prime_sum_improved
        ]
        n = pow(10, 10)
        expected = (9999419621, 41708)
        starts = []
        stops = []
        for solution in solutions:
            starts.append(perf_counter())
            self.assertTupleEqual(expected, solution(n))
            stops.append(perf_counter())
        print(f"Brute solution took: {stops[0] - starts[0]:0.2f}s\n" +
              f"Improved solution took: {stops[1] - starts[1]:0.2f}s\n")


if __name__ == '__main__':
    unittest.main()
