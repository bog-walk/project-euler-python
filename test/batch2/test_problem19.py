import unittest
from util.tests.reusable import compare_speed_seconds
from solution.batch2.problem19 import *


class CountingSundays(unittest.TestCase):
    def test_is_leap_year_all_true(self):
        years = [2016, 2020, 2000, 1980, 2396, 1944]
        for year in years:
            self.assertTrue(is_leap_year(year))

    def test_is_leap_year_all_false(self):
        years = [2100, 2200, 1900, 1986, 2379]
        for year in years:
            self.assertFalse(is_leap_year(year))

    def test_get_january_first(self):
        years = [1900, 1901, 1920, 1986, 2000, 2020]
        expected = [1, 2, 4, 3, 6, 3]
        for i, year in enumerate(years):
            self.assertEqual(expected[i], get_january_first(year))

    def test_get_weekday(self):
        dates = [[1, 1, 1900], [17, 10, 2021], [24, 8, 2000], [25, 12, 1982]]
        expected = [2, 1, 5, 0]
        for i, (d, m, y) in enumerate(dates):
            self.assertEqual(expected[i], get_weekday(d, m, y))

    def test_count_sunday_firsts_days_none(self):
        d1, m1, y1 = 31, 12, 1999
        d2, m2, y2 = 1, 1, 2000
        expected = 0
        self.assertEqual(expected, count_sundays_firsts(y1, m1, d1, y2, m2, d2))
        self.assertEqual(expected, count_sundays_zellers(y1, m1, d1, y2, m2))

    def test_count_sunday_firsts_days_one(self):
        d1, m1, y1 = 31, 12, 2022
        d2, m2, y2 = 1, 1, 2023
        expected = 1
        self.assertEqual(expected, count_sundays_firsts(y1, m1, d1, y2, m2, d2))
        self.assertEqual(expected, count_sundays_zellers(y1, m1, d1, y2, m2))

    def test_count_sunday_firsts_months(self):
        d1, m1, y1 = 10, 5, 2020
        d2, m2, y2 = 29, 11, 2020
        expected = 1
        self.assertEqual(expected, count_sundays_firsts(y1, m1, d1, y2, m2, d2))
        self.assertEqual(expected, count_sundays_zellers(y1, m1, d1, y2, m2))

    def test_count_sunday_firsts_years(self):
        d1, m1, y1 = 6, 12, 1995
        d2, m2, y2 = 2, 4, 1998
        expected = 5
        self.assertEqual(expected, count_sundays_firsts(y1, m1, d1, y2, m2, d2))
        self.assertEqual(expected, count_sundays_zellers(y1, m1, d1, y2, m2))

    def test_count_sunday_firsts_decade(self):
        d1, m1, y1 = 1, 1, 1900
        d2, m2, y2 = 1, 1, 1910
        expected = 18
        self.assertEqual(expected, count_sundays_firsts(y1, m1, d1, y2, m2, d2))
        self.assertEqual(expected, count_sundays_zellers(y1, m1, d1, y2, m2))

    def test_count_sunday_firsts_century(self):
        d1, m1, y1 = 1, 1, 1901
        d2, m2, y2 = 31, 12, 2000
        expected = 171
        self.assertEqual(expected, count_sundays_firsts(y1, m1, d1, y2, m2, d2))
        self.assertEqual(expected, count_sundays_zellers(y1, m1, d1, y2, m2))

    def test_count_sunday_firsts_adjusted_exceeds_end(self):
        d1, m1, y1 = 4, 1, 1900
        d2, m2, y2 = 10, 1, 1900
        expected = 0
        self.assertEqual(expected, count_sundays_firsts(y1, m1, d1, y2, m2, d2))
        self.assertEqual(expected, count_sundays_zellers(y1, m1, d1, y2, m2))

    def test_count_sunday_firsts_future(self):
        d1, m1, y1 = 12, 12, 4699
        d2, m2, y2 = 1, 1, 4710
        expected = 18
        self.assertEqual(expected, count_sundays_zellers(y1, m1, d1, y2, m2))
        self.assertEqual(expected, count_sundays_zellers(y1, m1, d1, y2, m2))

    def test_count_sunday_firsts_upper_constraint(self):
        d1, m1, y1 = 2, 2, 1_000_000_000_000
        d2, m2, y2 = 2, 3, 1_000_000_001_000
        expected = 1720
        self.assertEqual(expected, count_sundays_zellers(y1, m1, d1, y2, m2))

    def test_count_sunday_firsts_speed(self):
        d1, m1, y1 = 1, 1, 1_000_000
        d2, m2, y2 = 31, 12, 2_000_000
        solutions = {
            "Original": [count_sundays_firsts, y1, m1, d1, y2, m2, d2],
            "Zeller's": [count_sundays_zellers, y1, m1, d1, y2, m2]
        }
        results = list(compare_speed_seconds(solutions, precision=2).values())
        self.assertEqual(results[0], results[1])


if __name__ == '__main__':
    unittest.main()
