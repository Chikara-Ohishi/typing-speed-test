import random

class WordContainer:
    def __init__(self):
        self.word_list = None
        with open("frequent_words_1-2000.txt") as file:
            self.word_list = file.read().splitlines()
        self.init_list()

    def init_list(self):
        self.current_position = 0
        random.shuffle(self.word_list)

    def get_next(self):
        word = self.word_list[self.current_position]
        self.current_position += 1
        return word