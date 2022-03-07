import unittest
from util.tests.reusable import compare_speed, get_test_resource
from solution.batch1.problem11 import largest_row_product, largest_col_product, \
    largest_diagonal_product, largest_product_in_grid_functional,\
    largest_product_in_grid


class LargestProductInGrid(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.small_grid = get_test_resource(
            "../resources/largest_product_in_grid_4by4.txt", transformation=int
        )
        cls.mid_grid = get_test_resource(
            "../resources/largest_product_in_grid_6by6.txt", transformation=int
        )
        cls.large_grid = get_test_resource(
            "../resources/largest_product_in_grid_20by20.txt", transformation=int
        )

    def test_setup(self):
        self.assertEqual(20, len(self.large_grid))
        self.assertEqual(20, len(self.large_grid[0]))
        self.assertEqual(8, self.large_grid[0][0])
        self.assertEqual(48, self.large_grid[19][19])
        self.assertEqual(72, self.large_grid[15][7])

    def test_largest_row_product(self):
        self.assertEqual(3, largest_row_product(self.small_grid))
        self.assertEqual(15, largest_row_product(self.mid_grid))

    def test_largest_col_product(self):
        self.assertEqual(6, largest_col_product(self.small_grid))
        self.assertEqual(5, largest_col_product(self.mid_grid))

    def test_largest_diagonal_product(self):
        self.assertEqual(3, largest_diagonal_product(self.small_grid))
        self.assertEqual(1, largest_diagonal_product(self.mid_grid))

    def test_largest_product_in_grid(self):
        grids = [self.small_grid, self.mid_grid]
        expected = [6, 15]
        for i, grid in enumerate(grids):
            self.assertEqual(expected[i], largest_product_in_grid_functional(grid))
            self.assertEqual(expected[i], largest_product_in_grid(grid))

    def test_largest_product_in_grid_speed(self):
        grid = self.large_grid
        expected = 70_600_674
        solutions = {
            "Functional": [largest_product_in_grid_functional, grid],
            "All-in-one": [largest_product_in_grid, grid]
        }
        results = compare_speed(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))


if __name__ == '__main__':
    unittest.main()
