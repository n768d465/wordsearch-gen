from pprint import pprint
from wordgen import WordSearchGen
import random
from itertools import takewhile

class WordSearchmaker:

    def is_placeable(self, word, path):
        #print("Attempting to place: ", word, " with path ", path)
        if all(char.strip == ' ' for char in path):
            return True
        else:
            for char, step in zip(word, path):
                #print(char, step)
                if step != ' ':
                    if step != char:
                        return False

        print("Found successful path: ", path, " with word: ", word)
        return True

    def place_word(self, orientation, word, row, col):
        if orientation == "HORIZONTAL":
            for i in range(0, self.length):
                self.grid[row][i] = word['word'][i]
        elif orientation == "VERTICAL":
            for i in range(0, self.length):
                self.grid[i][col] = word['word'][i]
        elif orientation == "DIAGONAL":
            for i in range(0, self.length):
                self.grid[row + i][col+ i] = word['word'][i]

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

    def make_wordsearch(self):
        for word in self.words:
            placement_attempts = 0
            word_key = word['word']
            self.length = len(word_key)
            row_spot, col_spot = self._get_new_positions(word['orientation'])
            path = self._get_path(word['orientation'], row_spot, col_spot)

            if self.is_placeable(word_key, path):
                self.place_word(word['orientation'], word, row_spot, col_spot)
            else:
                while not self.is_placeable(word_key, path):
                    row_spot, col_spot = self._get_new_positions(word['orientation'])
                    path = self._get_path(word['orientation'], row_spot, col_spot)
                    placement_attempts += 1
                    if placement_attempts == self.max_attempts:
                        self.words = [words for words in self.words if words.get('word') != word['word']]
                        break
                else:
                    self.place_word(word['orientation'], word, row_spot, col_spot)


    def __init__(self, dim, words):
        self.dim = dim
        self.grid  = [[' ' for y in range(x * dim, x * dim + dim)] for x in range(dim)]
        self.wg = WordSearchGen(dim)
        self.words = self.wg.get_wordbank() if not len(words) else words
        self.max_attempts = 10
        self.length = 0

        self.make_wordsearch()

        pprint(self.grid, width=self.dim * 10)
        pprint(self.words)

def main():

    """
    words = [
        {
            "word": "trip",
            "orientation": "HORIZONTAL",
            "reversed": False
        },
        {
            "word": "bhim",
            "orientation": "VERTICAL",
            "reversed": False
        }
    ]
    """
    ws = WordSearchmaker(8, words = [])

if __name__ == '__main__':
        main()
        print()