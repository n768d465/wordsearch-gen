from pprint import pprint
from word_bank import get_wordbank, pull_word
from random import randint
from string import ascii_lowercase
from itertools import chain


class WordSearchGenerator:
    HORIZONTAL_COLOR = "\033[94m"
    VERTICAL_COLOR = "\033[92m"
    DIAGONAL_COLOR = "\033[93m"
    ENDC = "\033[0m"

    def _is_placeable(self, word, path):
        return not any(
            (step != " " and step != char) for (char, step) in zip(word, path)
        )

    def _place_char(self, ch, orientation):
        if orientation == "HORIZONTAL":
            return (self.HORIZONTAL_COLOR + ch + self.ENDC) if self.color_words else ch
        if orientation == "VERTICAL":
            return (self.VERTICAL_COLOR + ch + self.ENDC) if self.color_words else ch
        if orientation == "DIAGONAL":
            return (self.DIAGONAL_COLOR + ch + self.ENDC) if self.color_words else ch

    def _place_word(self, orientation, word, row, col):
        if orientation == "HORIZONTAL":
            it = enumerate(word, col)
        elif orientation == "VERTICAL":
            it = enumerate(word, row)
        elif orientation == "DIAGONAL":
            diag = min(row, col)
            it = enumerate(word, diag)

        for i, char in it:
            if orientation == "HORIZONTAL":
                self.grid[row][i] = self._place_char(char, orientation)
            elif orientation == "VERTICAL":
                self.grid[i][col] = self._place_char(char, orientation)
            elif orientation == "DIAGONAL":
                self.grid[i][i] = self._place_char(char, orientation)

    def _get_new_positions(self, orientation):
        if orientation == "HORIZONTAL":
            i = randint(0, self.dim - 1)
            j = randint(0, self.dim - 1 - 2)
        elif orientation == "VERTICAL":
            i = randint(0, self.dim - 1 - 2)
            j = randint(0, self.dim - 1)
        elif orientation == "DIAGONAL":
            i = randint(0, self.dim - 1 - 2)
            j = randint(0, self.dim - 1 - 2)

        return i, j

    def _get_path(self, orientation, row, col):
        if orientation == "HORIZONTAL":
            return self.grid[row][col:]
        elif orientation == "VERTICAL":
            return [self.grid[i][col] for i in range(row, self.dim)]
        elif orientation == "DIAGONAL":
            diag = min(row, col)
            return [self.grid[i][i] for i in range(diag, self.dim)]

    def _fill_remaining_spaces(self):
        self.grid = [
            [ascii_lowercase[(randint(0, 25))] if y == " " else y for y in x]
            for x in self.grid
        ]

    def _make_wordsearch(self):

        for _ in range(self.dim):
            ort = ("HORIZONTAL", "VERTICAL", "DIAGONAL")[randint(0, 2)]
            i, j = self._get_new_positions(ort)
            path = self._get_path(ort, i, j)
            path_len = len(path)

            placeable_words = set(
                filter(lambda w: self._is_placeable(w, path), self.words[path_len])
            )

            try:
                word = pull_word(placeable_words)
                self._place_word(ort, word, i, j)
                self.bank.append(word)
            except Exception:
                attempts = path_len - 1
                while attempts > 3:
                    placeable_words = set(
                        filter(
                            lambda w: self._is_placeable(w, path), self.words[attempts]
                        )
                    )
                    try:
                        word = pull_word(placeable_words)
                        self._place_word(ort, word, i, j)
                        self.bank.append(word)
                    except Exception:
                        pass
                    attempts = attempts - 1
                else:
                    continue

    def __init__(self, dim, words=[], color_words=False):
        self.dim = dim
        self.grid = [[" " for y in range(x * dim, x * dim + dim)] for x in range(dim)]
        self.words = get_wordbank(6) if not len(words) else words
        self.bank = []
        self.color_words = color_words if color_words else False
        self.max_attempts = 10
        self.length = 0
        self._make_wordsearch()


def run_wordsearch():
    dim = 8
    ws = WordSearchGenerator(dim=dim, color_words=False)

    for row in ws.grid:
        print(" ".join(row))

    print(ws.bank)


if __name__ == "__main__":
    run_wordsearch()
