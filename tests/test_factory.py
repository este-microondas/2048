import unittest
from game.factory import DifficultyFactory
from game.difficulty import EasyMode, HardMode


class TestFactory(unittest.TestCase):
    def test_create_easy(self):
        difficulty = DifficultyFactory.create_difficulty("easy")
        self.assertIsInstance(difficulty, EasyMode)

    def test_create_hard(self):
        difficulty = DifficultyFactory.create_difficulty("hard")
        self.assertIsInstance(difficulty, HardMode)

    def test_create_invalid(self):
        with self.assertRaises(ValueError):
            DifficultyFactory.create_difficulty("medium")


if __name__ == "__main__":
    unittest.main()