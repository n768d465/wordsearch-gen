from .word_sampler import sample_placeable_word
from random import choice, randint
from string import ascii_lowercase
from .path import path
from masterlist.builder import get_master_list


class WordSearchGenerator:
    def make_wordsearch(self, category, dim, min_word_length, max_word_length):
        self.grid = [[" "] * dim for _ in range(dim)]
        self.bank = set()
        self.ws_data = []

        max_words = randint(dim - 2, dim + 2)

        while len(self.bank) < max_words:
            _current_path = []
            _path_positions = []
            orientation = choice(
                ("HORIZONTAL", "VERTICAL", "DIAGONAL", "FORWARD DIAGONAL")
            )

            i, j = (randint(0, dim - 1), randint(0, dim - 1))

            for x, y, char in path(self.grid, orientation, i, j):
                _current_path.append(char)
                _path_positions.append((x, y))

            word_item = sample_placeable_word(
                self.word_list[category],
                min_word_length,
                max_word_length,
                _current_path,
            )

            if word_item and word_item.word2 not in self.bank:
                for (i, j), char in zip(_path_positions, word_item.word):
                    self.grid[i][j] = char
                    word_item.positions.append((i, j))
                self.bank.add(word_item.word2)
                self.ws_data.append(word_item)

        self.grid = [
            [choice(ascii_lowercase) if y == " " else y for y in x] for x in self.grid
        ]

    def __init__(self):
        self.grid = []
        self.bank = set()
        self.ws_data = []
        self.word_list = get_master_list()
