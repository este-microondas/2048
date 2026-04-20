import unittest
import os
from game.save_manager import SaveManager
from game.user import User


class TestSaveManager(unittest.TestCase):
    def setUp(self):
        self.file = "test_user_data.json"
        self.manager = SaveManager(self.file)

    def tearDown(self):
        if os.path.exists(self.file):
            os.remove(self.file)

    def test_save_and_load(self):
        user = User("TestUser")
        user.add_score(100)

        self.manager.save_user_data(user)

        data = self.manager.load_user_data("TestUser")

        self.assertIsNotNone(data)
        self.assertEqual(data["best_score"], 100)


if __name__ == "__main__":
    unittest.main()