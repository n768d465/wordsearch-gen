from word_bank import get_wordbank, pull_word
from random import randint, sample
from string import ascii_lowercase
import argparse


def is_placeable(word, path):
    return not any((step != " " and step != char) for (char, step) in zip(word, path))


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

    def _get_new_positions(self, orientation):
        i, j = sample(self.coords, 1)[0]
        self.coords.remove((i, j))
        return i, j

    def _get_path(self, orientation, row, col):
        if orientation == "HORIZONTAL":
            return [self.grid[row][i] for i in range(col, self.max_word_length)]
        elif orientation == "VERTICAL":
            return [self.grid[i][col] for i in range(row, self.max_word_length)]
        elif orientation == "DIAGONAL":
            diag = min(row, col)
            return [self.grid[i][i] for i in range(diag, self.max_word_length)]

    def _fill_remaining_spaces(self):
        self.grid = [
            [ascii_lowercase[(randint(0, 25))] if y == " " else y for y in x]
            for x in self.grid
        ]

    def _make_wordsearch(self):
        for _ in range(self.dim):
            placement_attempts = self.dim
            while placement_attempts > 0:
                ort = ("HORIZONTAL", "VERTICAL", "DIAGONAL")[randint(0, 2)]
                i, j = self._get_new_positions(ort)
                path = self._get_path(ort, i, j)
                path_len = len(path)

                possible_words = {
                    word for w in range(3, path_len) for word in self.words[w]
                }
                placeable_words = set(
                    filter(lambda w: is_placeable(w, path), possible_words)
                )

                try:
                    word = pull_word(placeable_words)
                    self._place_word(ort, word, i, j)
                    self.bank.add(word)
                    break
                except Exception:
                    placement_attempts = placement_attempts - 1
                    continue

        if self.fill:
            self._fill_remaining_spaces()

    def __init__(self, dim, words=[], fill=True):
        self.dim = dim
        self.fill = fill
        self.max_word_length = self.dim
        self.grid = [[" " for y in range(x * dim, x * dim + dim)] for x in range(dim)]
        self.coords = [(x, y) for x in range(self.dim) for y in range(self.dim)]
        self.words = get_wordbank(self.max_word_length) if not len(words) else words
        self.bank = set()
        self._make_wordsearch()


def run_wordsearch(dim, fill):
    ws = WordSearchGenerator(dim=dim, fill=fill)

    for row in ws.grid:
        print(" ".join(row))

    print(ws.bank)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Random wordsearch generator.")
    parser.add_argument("--dim", type=int, default=10)
    parser.add_argument("--no-fill", action="store_false")

    args = parser.parse_args()
    run_wordsearch(args.dim, args.no_fill)
