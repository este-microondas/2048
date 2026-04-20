import unittest
from game.board import Board


class TestBoard(unittest.TestCase):
    def test_board_creation(self):
        board = Board(4, 4)
        grid = board.get_grid()

        self.assertEqual(len(grid), 4)
        self.assertEqual(len(grid[0]), 4)

    def test_invalid_small_board(self):
        with self.assertRaises(ValueError):
            Board(3, 4)

    def test_invalid_large_board(self):
        with self.assertRaises(ValueError):
            Board(17, 4)

    def test_compress_row(self):
        board = Board(4, 4)
        row = [2, 0, 2, 4]
        result = board.compress_row(row)

        self.assertEqual(result, [2, 2, 4, 0])

    def test_merge_row(self):
        board = Board(4, 4)
        row = [2, 2, 4, 0]
        merged_row, score = board.merge_row(row)

        self.assertEqual(merged_row, [4, 0, 4, 0])
        self.assertEqual(score, 4)

    def test_has_empty_cell(self):
        board = Board(4, 4)
        self.assertTrue(board.has_empty_cell())

    def test_can_move_on_empty_board(self):
        board = Board(4, 4)
        self.assertTrue(board.can_move())


if __name__ == "__main__":
    unittest.main()