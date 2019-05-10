from word_bank import WordSampler
from random import choice, randint
from string import ascii_lowercase


class WordSearchGenerator:
    def _place_word(self, orientation, word, row, col):
        if orientation == "HORIZONTAL":
            for i, char in enumerate(word, col):
                self.grid[row][i] = char
        elif orientation == "VERTICAL":
            for i, char in enumerate(word, row):
                self.grid[i][col] = char
        elif orientation == "DIAGONAL":
            for i, char in zip(range(self.dim - max(row, col)), word):
                self.grid[row + i][col + i] = char

    def _get_path(self, orientation, i, j):
        if orientation == "HORIZONTAL":
            return [self.grid[i][n] for n in range(j, self.dim)]
        elif orientation == "VERTICAL":
            return [self.grid[n][j] for n in range(i, self.dim)]
        elif orientation == "DIAGONAL":
            return [self.grid[i + n][j + n] for n in range(self.dim - max(i, j))]

    def _fill_remaining_spaces(self):
        self.grid = [
            [choice(ascii_lowercase) if y == " " else y for y in x] for x in self.grid
        ]

    def _random_coords(self):
        return (randint(0, self.dim - 1), randint(0, self.dim - 1))

    def make_wordsearch(self):
        self.grid = [[" "] * self.dim for _ in range(self.dim)]
        if self.max_word_length > self.dim:
            raise ValueError("Max word length is larger than the grid size.")

        while len(self.bank) < self.max_words:
            ort = choice(("HORIZONTAL", "VERTICAL", "DIAGONAL"))
            i, j = self._random_coords()
            path = self._get_path(ort, i, j)
            word = self.wb.sample_placeable_word(path)
            if word:
                self._place_word(ort, word, i, j)
                self.bank.add(word)

        if self.fill:
            self._fill_remaining_spaces()

    def __init__(self, dim=10, max_word_length=10, fill=True):
        self.dim = dim
        self.fill = fill
        self.max_word_length = max_word_length
        self.grid = [[]]
        self.bank = set()
        self.max_words = randint(self.dim - 2, self.dim + 2)
        self.wb = WordSampler(self.max_word_length)

