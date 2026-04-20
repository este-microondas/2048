from game.difficulty import EasyMode, HardMode


class DifficultyFactory:
    @staticmethod
    def create_difficulty(choice):
        if choice == "easy":
            return EasyMode()
        if choice =="hard":
            return HardMode()
        raise ValueError("Invalid difficulty")