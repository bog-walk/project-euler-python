import unittest
from solution.batch2.problem11 import largest_row_product, largest_col_product, \
    largest_diagonal_product, largest_product_in_grid


def get_test_grid(filename):
    with open(filename) as gridFile:
        grid = [list(map(lambda n: int(n), row.strip().split(" "))) for row in gridFile]
    return grid


class LargestProductInGrid(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.small_grid = get_test_grid("../resources/largest_product_in_grid_4by4")
        cls.mid_grid = get_test_grid("../resources/largest_product_in_grid_6by6")
        cls.large_grid = get_test_grid("../resources/largest_product_in_grid_20by20")

    def test_grid_setup(self):
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
        self.assertEqual(6, largest_product_in_grid(self.small_grid))
        self.assertEqual(15, largest_product_in_grid(self.mid_grid))
        self.assertEqual(70600674, largest_product_in_grid(self.large_grid))


if __name__ == '__main__':
    unittest.main()
