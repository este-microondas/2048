import json
import os


class SaveManager:
    def __init__(self, file_name="user_data.json"):
        self.file_name = os.path.join(os.path.dirname(__file__), file_name)

    def load_all_users(self):
        if not os.path.exists(self.file_name):
            return {}

        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {}

    def save_user_data(self, user):
        all_users = self.load_all_users()

        all_users[user.get_name()] = {
            "score": user.get_score(),
            "best_score": user.get_best_score()
        }

        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(all_users, file, indent=4)

    def load_user_data(self, user_name):
        all_users = self.load_all_users()
        return all_users.get(user_name)