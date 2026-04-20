class User:
    def __init__(self, name):
        self.__name = name
        self.__score = 0
        self.__best_score = 0

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def get_best_score(self):
        return self.__best_score

    def add_score(self, points):
        self.__score += points
        if self.__score > self.__best_score:
            self.__best_score = self.__score

    def reset_score(self):
        self.__score = 0

    def set_best_score(self, best_score):
        self.__best_score = best_score