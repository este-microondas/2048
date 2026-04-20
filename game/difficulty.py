import random

class Difficulty:
    def get_new_tile_value(self):
        raise NotImplementedError("This mettod must be overridden")

class EasyMode(Difficulty):
    def get_new_tile_value(self):
        return 2

class HardMode(Difficulty):
    def get_new_tile_value(self):
        return random.choice([2, 4])