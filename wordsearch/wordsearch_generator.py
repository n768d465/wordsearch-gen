from .word_sampler import create_sampler
from random import choice, randint
from string import ascii_lowercase


class WordSearchGenerator:
    def _place_word(self, word_item):
        word = word_item["word"][::-1] if word_item["reversed"] else word_item["word"]
        for (i, j), char in zip(self._path_positions, word):
            self.grid[i][j] = char
            word_item["positions"].append((i, j))

    def _get_path(self, orientation, i, j):
        grid_len = len(self.grid)
        self._current_path = []
        self._path_positions = []

        if orientation == "HORIZONTAL":
            for k, n in enumerate(self.grid[i][j:]):
                self._current_path.append(self.grid[i][k])
                self._path_positions.append((i, k))
        if orientation == "VERTICAL":
            for k, _ in enumerate(self.grid):
                self._current_path.append(self.grid[k][j])
                self._path_positions.append((k, j))
        if orientation == "DIAGONAL":
            for x, y in zip(range(i, grid_len), range(j, grid_len)):
                self._current_path.append(self.grid[i][j])
                self._path_positions.append((i, j))
        if orientation == "FORWARD DIAGONAL":
            for x, y in zip(range(i, -1, -1), range(j, grid_len)):
                self._current_path.append(self.grid[i][j])
                self._path_positions.append((i, j))

    def _fill_remaining_spaces(self):
        self.grid_words_only = [[r for r in row] for row in self.grid]
        self.grid = [
            [choice(ascii_lowercase) if y == " " else y for y in x] for x in self.grid
        ]

    def make_wordsearch(self):
        self.grid = [[" "] * self.dim for _ in range(self.dim)]
        if self.max_word_length > self.dim:
            raise ValueError("Max word length is larger than the grid size.")

        while len(self.bank) < self.max_words:
            ort = choice(("HORIZONTAL", "VERTICAL", "DIAGONAL", "FORWARD DIAGONAL"))
            i, j = (randint(0, self.dim - 1), randint(0, self.dim - 1))

            self._get_path(ort, i, j)
            word_item = self.sample_word(self._current_path)
            if word_item:
                self._place_word(word_item)
                self.bank.add(word_item["word"])
                self.ws_data.append(word_item)

        self._fill_remaining_spaces()

    def __init__(self, dim=10, max_word_length=7):
        self.dim = int(dim)
        self.max_word_length = int(max_word_length)
        self.grid = [[]]
        self.grid_words_only = [[]]
        self.bank = set()
        self.ws_data = []
        self.max_words = randint(self.dim - 2, self.dim + 2)
        self.sample_word = create_sampler(self.max_word_length)
        self._current_path = []
        self._path_positions = []

