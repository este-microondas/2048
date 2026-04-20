import random


class Board:
    def __init__(self, rows=4, cols=4):
        if rows < 4 or cols < 4:
            raise ValueError("Minimum size is 4x4")

        if rows > 16 or cols > 16:
            raise ValueError("Maximum size is 16x16")

        self.__rows = rows
        self.__cols = cols
        self.__grid = [[0 for _ in range(cols)] for _ in range(rows)]

    def get_grid(self):
        return self.__grid

    def add_tile(self, value):
        empty = []

        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.__grid[i][j] == 0:
                    empty.append((i, j))

        if empty:
            row, col = random.choice(empty)
            self.__grid[row][col] = value

    def print_board(self):
        width = 5  # width per cell including |
        total_width = self.__cols * width + 1
        print('—' * total_width)
        for row in self.__grid:
            print('|', end='')
            for cell in row:
                print(f'{cell:4}|', end='')
            print()
        print('—' * total_width)

    def compress_row(self, row):
        new_row = [num for num in row if num != 0]

        while len(new_row) < self.__cols:
            new_row.append(0)

        return new_row

    def merge_row(self, row):
        score = 0

        for i in range(self.__cols - 1):
            if row[i] != 0 and row[i] == row[i + 1]:
                row[i] *= 2
                score += row[i]
                row[i + 1] = 0

        return row, score

    def reverse_rows(self, grid):
        return [row[::-1] for row in grid]

    def transpose(self, grid):
        return [list(row) for row in zip(*grid)]

    def move_left(self):
        new_grid = []
        total_score = 0
        moved = False

        for row in self.__grid:
            compressed = self.compress_row(row)
            merged, score = self.merge_row(compressed)
            final_row = self.compress_row(merged)

            if final_row != row:
                moved = True

            new_grid.append(final_row)
            total_score += score

        self.__grid = new_grid
        return moved, total_score

    def move_right(self):
        self.__grid = self.reverse_rows(self.__grid)
        moved, score = self.move_left()
        self.__grid = self.reverse_rows(self.__grid)
        return moved, score

    def move_up(self):
        self.__grid = self.transpose(self.__grid)
        moved, score = self.move_left()
        self.__grid = self.transpose(self.__grid)
        return moved, score

    def move_down(self):
        self.__grid = self.transpose(self.__grid)
        self.__grid = self.reverse_rows(self.__grid)
        moved, score = self.move_left()
        self.__grid = self.reverse_rows(self.__grid)
        self.__grid = self.transpose(self.__grid)
        return moved, score

###CHECKING##
    def has_empty_cell(self):
        for row in self.__grid:
            if 0 in row:
                return True
        return False

    def has_winning_tile(self):
        for row in self.__grid:
            for value in row:
                if value == 2048:
                    return True
        return False

    def can_move(self):
        if self.has_empty_cell():
            return True

        for i in range(self.__rows):
            for j in range(self.__cols - 1):
                if self.__grid[i][j] == self.__grid[i][j + 1]:
                    return True

        for j in range(self.__cols):
            for i in range(self.__rows - 1):
                if self.__grid[i][j] == self.__grid[i + 1][j]:
                    return True

        return False