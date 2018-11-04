from pprint import pprint
from word_bank import get_wordbank
import random
import string

HORIZONTAL_COLOR = "\033[94m"
VERTICAL_COLOR = "\033[92m"
DIAGONAL_COLOR = "\033[93m"
ENDC = "\033[0m"


class WordSearchGenerator:
    def _is_placeable(self, word, path):
        return not any(
            (step != " " and step != char) for (char, step) in zip(word, path)
        )

    def _place_char(self, ch, orientation):
        if orientation == "HORIZONTAL":
            return (HORIZONTAL_COLOR + ch + ENDC) if self.color_words else ch
        if orientation == "VERTICAL":
            return (VERTICAL_COLOR + ch + ENDC) if self.color_words else ch
        if orientation == "DIAGONAL":
            return (DIAGONAL_COLOR + ch + ENDC) if self.color_words else ch

    def _place_word(self, orientation, word, row, col):
        for i, char in enumerate(word):
            if orientation == "HORIZONTAL":
                self.grid[row][i] = self._place_char(char, orientation)
            elif orientation == "VERTICAL":
                self.grid[i][col] = self._place_char(char, orientation)
            elif orientation == "DIAGONAL":
                self.grid[row + i][col + i] = self._place_char(char, orientation)

    def _get_new_positions(self, orientation):
        if orientation == "HORIZONTAL":
            max_row_randint_range = self.dim - 1
            max_col_randint_range = abs(self.dim - self.length)
        elif orientation == "VERTICAL":
            max_row_randint_range = abs(self.dim - self.length)
            max_col_randint_range = self.dim - 1
        elif orientation == "DIAGONAL":
            max_row_randint_range = abs(self.dim - self.length)
            max_col_randint_range = abs(self.dim - self.length)

        row = random.randint(0, max_row_randint_range)
        col = random.randint(0, max_col_randint_range)
        return row, col

    def _get_path(self, orientation, row, col):
        if orientation == "HORIZONTAL":
            return [self.grid[row][i] for i in range(self.length)]
        elif orientation == "VERTICAL":
            return [self.grid[i][col] for i in range(self.length)]
        elif orientation == "DIAGONAL":
            return [self.grid[row + i][col + i] for i in range(self.length)]

    def _fill_remaining_spaces(self):
        self.grid = [
            [
                string.ascii_lowercase[(random.randint(0, 25))] if y == " " else y
                for y in x
            ]
            for x in self.grid
        ]

    def _make_wordsearch(self):
        for word in self.words:
            placement_attempts = 0
            word_key = (word["word"])[::-1] if word["reversed"] else word["word"]
            self.length = len(word_key)
            row_spot, col_spot = self._get_new_positions(word["orientation"])
            path = self._get_path(word["orientation"], row_spot, col_spot)

            while not self._is_placeable(word_key, path):
                row_spot, col_spot = self._get_new_positions(word["orientation"])
                path = self._get_path(word["orientation"], row_spot, col_spot)
                placement_attempts += 1
                if placement_attempts == self.max_attempts:
                    self.words = [
                        words
                        for words in self.words
                        if words.get("word") != word["word"]
                    ]
                    break
            else:
                self._place_word(word["orientation"], word_key, row_spot, col_spot)

        self._fill_remaining_spaces()

    def __init__(self, dim, words, color_words):
        self.dim = dim
        self.grid = [[" " for y in range(x * dim, x * dim + dim)] for x in range(dim)]
        self.words = get_wordbank(dim) if not len(words) else words
        self.color_words = color_words if color_words else False
        self.max_attempts = 10
        self.length = 0
        self._make_wordsearch()


def main():
    ws = WordSearchGenerator(int(input()), words=[], color_words=True)

    for row in ws.grid:
        print(" ".join(row))
    pprint([word["word"] for word in ws.words])


if __name__ == "__main__":
    main()
