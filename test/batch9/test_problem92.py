import unittest
from util.tests.reusable import compare_speed
from solution.batch9.problem92 import count_sd_chains_brute, count_sd_chains


class SquareDigitChains(unittest.TestCase):
    def test_lower_constraints(self):
        expected = [7, 80, 857, 8558, 85623, 856_929]
        for k in range(1, 7):
            self.assertEqual(expected[k-1], count_sd_chains_brute(k))
            self.assertEqual(expected[k-1], count_sd_chains(k))

    def test_lower_constraint_speed(self):
        k = 7
        expected = 8_581_146
        solutions = {
            "Brute": [count_sd_chains_brute, k],
            "Improved": [count_sd_chains, k],
        }    
        results = compare_speed(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))

    def test_lower_mid_constraints(self):
        expected = [85_744_333, 854_325_192, 507_390_796]
        for k in range(8, 11):
            self.assertEqual(expected[k-8], count_sd_chains(k))

    def test_mid_constraints(self):
        inputs = [20, 50, 73]
        expected = [742_248_133, 428_414_150, 319_026_233]
        for k, e in zip(inputs, expected):
            self.assertEqual(e, count_sd_chains(k))

    def test_upper_constraints(self):
        inputs = [100, 200]
        expected = [999_578_314, 237_156_061]
        for k, e in zip(inputs, expected):
            self.assertEqual(e, count_sd_chains(k))
        
        
if __name__ == '__main__':
    unittest.main()
