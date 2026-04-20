from game.board import Board
from game.difficulty import EasyMode, HardMode
from game.user import User
from game.save_manager import SaveManager
from game.input_handler import InputHandler
from game.factory import DifficultyFactory


class Game:
    def __init__(self):
        self.user = None
        self.board = None
        self.difficulty = None
        self.save_manager = SaveManager()
        self.input_handler = InputHandler()

    def create_user(self):
        while True:
            name = input("Enter your name: ").strip()
            if name:
                self.user = User(name)
                break
            print("Name cannot be empty. Try again.")

    def load_user_progress(self):
        data = self.save_manager.load_user_data(self.user.get_name())

        if data is not None:
            self.user.set_best_score(data["best_score"])
            print("Previous profile loaded.")
        else:
            print("New profile created.")

    def choose_board_size(self):
        while True:
            try:
                rows = int(input("Enter board rows (4-16): "))
                cols = int(input("Enter board cols (4-16): "))
                self.board = Board(rows, cols)
                break
            except ValueError as error:
                print(error)
                print("Try again.")

    def choose_difficulty(self):
        while True:
            choice = input("Choose difficulty (easy/hard): ").lower()

            try:
                self.difficulty = DifficultyFactory.create_difficulty(choice)
                break
            except ValueError:
                print("Invalid input. Try again.")

    def handle_move(self, move):
        if move == "left":
            return self.board.move_left()
        if move == "right":
            return self.board.move_right()
        if move == "up":
            return self.board.move_up()
        if move == "down":
            return self.board.move_down()
        return False, 0

    def start(self):
        self.create_user()
        self.load_user_progress()
        self.choose_board_size()
        self.choose_difficulty()

        self.board.add_tile(self.difficulty.get_new_tile_value())
        self.board.add_tile(self.difficulty.get_new_tile_value())


##HOLD GAME + checking((win/lose)link to board.py)
        while True:
            print(f"\nPlayer: {self.user.get_name()}")
            print(f"Score: {self.user.get_score()}")
            print(f"Best score: {self.user.get_best_score()}")
            print("Use WASD keys to move. Press Q to quit.")
            self.board.print_board()

            if self.board.has_winning_tile():
                print("You reached 2048! You win!")
                self.save_manager.save_user_data(self.user)
                break

            if not self.board.can_move():
                print("Game over!")
                self.save_manager.save_user_data(self.user)
                break

            move = self.input_handler.get_input()

            if move == "quit":
                self.save_manager.save_user_data(self.user)
                print("Game saved. Goodbye.")
                break

            moved, gained_score = self.handle_move(move)

            if moved:
                self.user.add_score(gained_score)
                self.board.add_tile(self.difficulty.get_new_tile_value())
            else:
                print("Invalid move or no tiles moved.")