from word_bank import WordBank
from random import choice, randint
from string import ascii_lowercase
import argparse


def enumerate_with_orientation(ort, word, row, col):
    if ort == "HORIZONTAL":
        it = enumerate(word, col)
    elif ort == "VERTICAL":
        it = enumerate(word, row)
    elif ort == "DIAGONAL":
        diag = min(row, col)
        it = enumerate(word, diag)

    return it


class WordSearchGenerator:
    def _place_word(self, orientation, word, row, col):
        it = enumerate_with_orientation(orientation, word, row, col)
        for i, char in it:
            if orientation == "HORIZONTAL":
                self.grid[row][i] = char
            elif orientation == "VERTICAL":
                self.grid[i][col] = char
            elif orientation == "DIAGONAL":
                self.grid[i][i] = char

    def _get_path(self, orientation, row, col):
        if orientation == "HORIZONTAL":
            return [self.grid[row][i] for i in range(col, self.dim)]
        elif orientation == "VERTICAL":
            return [self.grid[i][col] for i in range(row, self.dim)]
        elif orientation == "DIAGONAL":
            diag = min(row, col)
            return [self.grid[i][i] for i in range(diag, self.dim)]

    def _fill_remaining_spaces(self):
        self.grid = [
            [choice(ascii_lowercase) if y == " " else y for y in x] for x in self.grid
        ]

    def make_wordsearch(self):
        if self.max_word_length > self.dim:
            raise ValueError("Max word length is larger than the grid size.")

        while len(self.bank) < self.max_words:
            ort = choice(("HORIZONTAL", "VERTICAL", "DIAGONAL"))
            i, j = choice(self.coords)
            path = self._get_path(ort, i, j)
            word = next(self.wb.placeable_words(path))
            if word and len(self.bank) < self.max_words:
                self._place_word(ort, word, i, j)
                self.bank.add(word)
                self.coords.remove((i, j))

        if self.fill:
            self._fill_remaining_spaces()

    def __init__(self, dim, max_word_length=7, words=[], fill=True):
        self.dim = dim
        self.fill = fill
        self.max_word_length = max_word_length
        self.grid = [[" " for y in range(x * dim, x * dim + dim)] for x in range(dim)]
        self.coords = [(x, y) for x in range(self.dim) for y in range(self.dim)]
        self.bank = set()
        self.max_words = randint(self.dim - 2, self.dim + 5)
        self.wb = WordBank(self.max_word_length)


def run_wordsearch(dim, fill, length):
    ws = WordSearchGenerator(dim=dim, fill=fill, max_word_length=length)
    ws.make_wordsearch()

    print()
    for row in ws.grid:
        print(" ".join(row))

    print("\nWord bank")
    print("---------")
    for word in ws.bank:
        print(word, end=" ")
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Random wordsearch generator.")
    parser.add_argument("--dim", type=int, default=10)
    parser.add_argument("--no-fill", action="store_false")
    parser.add_argument("--max-word-length", type=int, default=7)

    args = parser.parse_args()

    run_wordsearch(args.dim, args.no_fill, args.max_word_length)
