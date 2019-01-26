from word_bank import get_wordbank, pull_word
from random import randint
from string import ascii_lowercase


class WordSearchGenerator:
    def _is_placeable(self, word, path):
        return not any(
            (step != " " and step != char) for (char, step) in zip(word, path)
        )

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
                self.grid[row][i] = char
            elif orientation == "VERTICAL":
                self.grid[i][col] = char
            elif orientation == "DIAGONAL":
                self.grid[i][i] = char

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
            placement_attempts = self.dim - 1
            reverse_criteria_met = randint(0, 10) >= 7
            while placement_attempts > 0:
                ort = ("HORIZONTAL", "VERTICAL", "DIAGONAL")[randint(0, 2)]
                i, j = self._get_new_positions(ort)
                path = self._get_path(ort, i, j)
                path_len = len(path)
                placeable_words = set(
                    filter(lambda w: self._is_placeable(w, path), self.words[path_len])
                )

                try:
                    word = pull_word(placeable_words)
                    if reverse_criteria_met:
                        reversed_word = word[::-1]
                        self._place_word(ort, reversed_word, i, j)
                    else:
                        self._place_word(ort, word, i, j)
                    self.bank.append(word)
                    break
                except Exception:
                    placement_attempts = placement_attempts - 1
                    continue

        self._fill_remaining_spaces()

    def __init__(self, dim, words=[]):
        self.dim = dim
        self.grid = [[" " for y in range(x * dim, x * dim + dim)] for x in range(dim)]
        self.words = get_wordbank(dim) if not len(words) else words
        self.bank = []
        self._make_wordsearch()


def run_wordsearch():
    dim = 10
    ws = WordSearchGenerator(dim=dim)

    for row in ws.grid:
        print(" ".join(row))

    print(ws.bank)


if __name__ == "__main__":
    run_wordsearch()
