from copy import deepcopy
from itertools import chain
from functools import reduce


class SudokuGame:
    """
    A Su Doku puzzle grid, with each cell value stored as a Set, so that options
    can be iterated over until a final value remains.
    """

    def __init__(self, cells: list[str]):
        if len(cells) != 9:
            raise ValueError("Su Doku grid requires 9 rows")
        if any(len(c) != 9 or not c.isdigit() for c in cells):
            raise ValueError("Input contains invalid characters")

        self.puzzle_cells = []
        for r in range(9):
            row = []
            for c in range(9):
                digit = int(cells[r][c])
                row.append({digit} if digit else {1, 2, 3, 4, 5, 6, 7, 8, 9})
            self.puzzle_cells.append(row)

    def has_unfilled_cells(self) -> bool:
        return any(len(c) != 1 for r in self.puzzle_cells for c in r)

    def get_grid(self, with_options: bool = False) -> list[str]:
        grid = []
        for row in self.puzzle_cells:
            row_s = ""
            for cell in row:
                # PY does not allow index access to sets
                row_s += str(cell) if with_options else \
                    "0" if len(cell) > 1 else str(cell).strip("{}")
            grid.append(row_s)
        return grid

    def reduce(self) -> [bool, bool]:
        while self.has_unfilled_cells():
            updated = False
            for row in range(9):
                for col in range(9):
                    if len(self.puzzle_cells[row][col]) == 1:
                        continue
                    filtered = self.__grid_filter(self.puzzle_cells[row][col], row, col)
                    if not len(filtered):
                        return updated, False
                    self.puzzle_cells[row][col] = filtered
                    if len(filtered) == 1:
                        updated = True
                        self.__clear_digits(row, col, filtered)
            if not updated:
                updated = self.__clear_by_assumption()
            if not updated:
                updated = self.__clear_by_pair_assumption()
            if not updated:
                return False, True

        return True, True

    def solve(self) -> bool:
        """
        Solves puzzle by attempting to reduce all possible values, until no
        changes are made, then a guess is made. So few puzzles make it to the
        guess stage, but the latter could potentially be optimised by finding the
        first unsolved cell with the least options.
        """

        was_updated, is_valid = self.reduce()
        if not is_valid:
            return False

        if not was_updated:
            # [].copy() returns only a shallow copy of the 2D grid
            og_version = deepcopy(self.puzzle_cells)
            for row in range(9):
                for col in range(9):
                    if len(self.puzzle_cells[row][col]) == 1:
                        continue
                    guesses = sorted(self.puzzle_cells[row][col])
                    for guess in guesses:
                        self.puzzle_cells[row][col] = {guess}
                        self.__clear_digits(row, col, {guess})
                        if self.solve() and \
                                all(len(set(map(tuple, r))) == 9
                                    for r in self.puzzle_cells):
                            return True
                        for r in range(9):  # simple assignment will not copy suitably
                            for c in range(9):
                                self.puzzle_cells[r][c] = og_version[r][c]

        return True

    def __grid_filter(self, to_filter: set[int], row_i: int,
                      col_i: int) -> set[int]:
        """
        Accesses the row, column, and box cells associated with a cell at
        [row_i][col_i] and performs 2 actions:
                - Reduces the set of possible values based on already filled cell
                values.
                - Checks if the newly reduced set contains a value that is not
                present in any of the other cells for each group. This will be
                returned as a priority; otherwise, the reduced set will be returned.
        """

        row_f, row_e, col_f, col_e = [], [], [], []
        for i in range(9):
            if i != col_i:
                to_add = self.puzzle_cells[row_i][i]
                row_f.append(to_add) if len(to_add) == 1 else row_e.append(to_add)
            to_add: set[int] = set() if i == row_i else self.puzzle_cells[i][col_i]
            col_f.append(to_add) if len(to_add) == 1 else col_e.append(to_add)

        box_f, box_e = [], []
        top_row, top_col = row_i // 3 * 3, col_i // 3 * 3
        for row in range(top_row, top_row + 3):
            if row == row_i:
                others = set([c for c in range(top_col, top_col + 3)]) - {col_i}
                for o in others:
                    to_add = self.puzzle_cells[row][o]
                    box_f.append(to_add) if len(to_add) == 1 else box_e.append(to_add)
            else:
                for col in range(top_col, top_col + 3):
                    to_add = self.puzzle_cells[row][col]
                    box_f.append(to_add) if len(to_add) == 1 else box_e.append(to_add)

        box_f_flat = set(chain(*box_f))
        row_f_flat = set(chain(*row_f))
        col_f_flat = set(chain(*col_f))
        reduced = to_filter - box_f_flat.union(row_f_flat).union(col_f_flat)
        empties = [set(chain(*box_e)), set(chain(*row_e)), set(chain(*col_e))]
        for group in empties:
            single = reduced - group
            if len(single) == 1:
                return single
        return reduced

    def __clear_digits(self, row_i: int, col_i: int, digits: set[int],
                       clear_box: bool = True, clear_row: bool = True,
                       clear_col: bool = True):
        """
        Supplementary action that clears the value of a newly filled cell from
        all associated row, column, and box cells. Speed has not been compared,
        but introducing this second step reduced the overall amount of iterations
        over the entire puzzle grid.
        """

        changed = False

        top_row, top_col = row_i // 3 * 3, col_i // 3 * 3
        for i in range(9):
            if clear_box:
                if len(self.puzzle_cells[i // 3 + top_row][i % 3 + top_col]) > 1:
                    cleared = self.puzzle_cells[i // 3 + top_row][
                                  i % 3 + top_col] - digits
                    self.puzzle_cells[i // 3 + top_row][i % 3 + top_col] = cleared
                    if len(cleared) == 1:
                        changed = True
                        self.__clear_digits(i // 3 + top_row, i % 3 + top_col, cleared)
            if clear_row:
                if (i < top_col or i > top_col + 2) and \
                        len(self.puzzle_cells[row_i][i]) > 1:
                    cleared = self.puzzle_cells[row_i][i] - digits
                    self.puzzle_cells[row_i][i] = cleared
                    if len(cleared) == 1:
                        changed = True
                        self.__clear_digits(row_i, i, cleared)
            if clear_col:
                if (i < top_row or i > top_row + 2) and \
                        len(self.puzzle_cells[i][col_i]) > 1:
                    cleared = self.puzzle_cells[i][col_i] - digits
                    self.puzzle_cells[i][col_i] = cleared
                    if len(cleared) == 1:
                        changed = True
                        self.__clear_digits(i, col_i, cleared)

        return changed

    def __clear_by_assumption(self) -> bool:
        """
        For situations when potential values in a box exist on a single
        column/row, thereby assuring that that column/row must contain the value.
        This assumption can be used to reduce set options in the corresponding
        column/row outside the box.
        """

        changed = False

        for box_i in range(9):
            top_row, top_col = box_i // 3 * 3, box_i % 3 * 3
            row_options = [list(
                filter(lambda s: len(s) > 1,
                       self.puzzle_cells[top_row + i][top_col:top_col + 3])
            ) for i in range(3)]

            for i, row in enumerate(row_options):
                if len(row) > 1:
                    options = reduce(lambda x, y: x.union(y), row)
                    others = set(o for o in range(top_row, top_row + 3)) - {top_row + i}
                    other_options = []
                    for o in others:
                        other_options += row_options[o % 3]
                    outliers = options if not len(other_options) else \
                        options - reduce(lambda x, y: x.union(y), other_options)
                    if not len(outliers):
                        continue
                    if self.__clear_digits(top_row + i, top_col, outliers,
                                           clear_box=False, clear_col=False):
                        changed = True

            col_options = [list(filter(lambda s: len(s) > 1,
                                       [self.puzzle_cells[top_row][top_col + i],
                                        self.puzzle_cells[top_row + 1][top_col + i],
                                        self.puzzle_cells[top_row + 2][top_col + i]]))
                           for i in range(3)]

            for i, col in enumerate(col_options):
                if len(col) > 1:
                    options = reduce(lambda x, y: x.union(y), col)
                    others = set(o for o in range(top_col, top_col + 3)) - {top_col + i}
                    other_options = []
                    for o in others:
                        other_options += col_options[o % 3]
                    outliers = options if not len(other_options) else \
                        options - reduce(lambda x, y: x.union(y), other_options)
                    if not len(outliers):
                        continue
                    if self.__clear_digits(top_row, top_col + i, outliers,
                                           clear_box=False, clear_row=False):
                        changed = True

        return changed

    def __clear_by_pair_assumption(self) -> bool:
        """
        For situations when potential values in a box exist as a pair; i.e.
        choosing one in a cell means the other cell must contain the other. If 2
        cells have identical sets containing only 2 values, these values can be
        filtered from all other cells in the box. Could then be followed by another
        call to clear_by_assumption() but this eventually occurs.
        """

        changed = False

        for box_i in range(9):
            top_row, top_col = box_i // 3 * 3, box_i % 3 * 3
            empty_pair_cells = list(
                filter(lambda s: len(s) == 2,
                       [self.puzzle_cells[top_row + i // 3][top_col + i % 3]
                        for i in range(9)])
            )
            # PY sets are unhashable type, so cannot get distinct objects without
            # e.g. converting to a hashable type, like a tuple, or using a separate list
            checked = []
            for pair in empty_pair_cells:
                if pair in checked:
                    continue
                if empty_pair_cells.count(pair) == 2:
                    for i in range(9):
                        cell = self.puzzle_cells[top_row + i // 3][top_col + i % 3]
                        if len(cell) == 1 or cell == pair:
                            continue
                        cleared = cell - pair
                        if len(cleared) < len(cell):
                            self.puzzle_cells[top_row + i // 3][top_col + i % 3] = cleared
                            changed = True
                            if len(cleared) == 1:
                                self.__clear_digits(top_row + i // 3, top_col + i % 3,
                                                    cleared)
                    checked.append(pair)

        return changed
