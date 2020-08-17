from .word_sampler import Sampler
from random import choice, randint
from string import ascii_lowercase
from .path import path


class WordSearchGenerator:
    def _place_word(self, word_item):
        word = word_item["word"][::-1] if word_item["reversed"] else word_item["word"]
        for (i, j), char in zip(self._path_positions, word):
            self.grid[i][j] = char
            word_item["positions"].append((i, j))

    def _form_current_path(self, orientation, i, j):
        self._current_path = []
        self._path_positions = []

        for x, y, char in path(self.grid, orientation, i, j):
            self._current_path.append(char)
            self._path_positions.append((x, y))

    def _fill_remaining_spaces(self):
        self.grid_words_only = [[r for r in row] for row in self.grid]
        self.grid = [
            [choice(ascii_lowercase) if y == " " else y for y in x] for x in self.grid
        ]

    def _clear_params(self):
        self.grid = [[" "] * self.dim for _ in range(self.dim)]
        self.grid_words_only = [[]]
        self.bank = set()
        self.ws_data = [[]]

    def make_wordsearch(self):
        self._clear_params()
        self.max_words = randint(self.dim - 2, self.dim + 2)
        self.sample_placeable_word.word_range = range(
            self.min_word_length, self.max_word_length
        )
        self.sample_placeable_word.category = self.category

        while len(self.bank) < self.max_words:
            ort = choice(("HORIZONTAL", "VERTICAL", "DIAGONAL", "FORWARD DIAGONAL"))
            i, j = (randint(0, self.dim - 1), randint(0, self.dim - 1))

            self._form_current_path(ort, i, j)
            word_item = self.sample_placeable_word(self._current_path)
            if word_item and word_item["word"] not in self.bank:
                self._place_word(word_item)
                self.bank.add(word_item["word"])
                self.ws_data.append(word_item)

        self._fill_remaining_spaces()

    def __init__(self, category="", dim=10, min_word_length=3, max_word_length=7):
        self.category = category
        self.dim = dim
        self.min_word_length = min_word_length
        self.max_word_length = max_word_length
        self.grid = [[]]
        self.grid_words_only = [[]]
        self.bank = set()
        self.ws_data = []
        self.max_words = randint(self.dim - 2, self.dim + 2)
        self.sample_placeable_word = Sampler(category, min_word_length, max_word_length)
        self._current_path = []
        self._path_positions = []
