from pprint import pprint
from wordgen import WordSearchGen
import random
from itertools import takewhile

class WordSearchmaker:
    def is_placeable(self, word, path):
        if not all(char.strip() == '' for char in path):
            for i, item in enumerate(path):
                if word[i] != item:
                    return False
            
        return True
            
    def place_diagonal_word(self, word, row, col):
        for i in range(0, self.length):
            self.grid[row + i][col+ i] = word['word'][i]
        self.word_bank.append(word)

    def place_horizontal_word(self, word, row):
        for i in range(0, self.length):
            self.grid[row][i] = word['word'][i]
        self.word_bank.append(word)

    def place_vertical_word(self, word, row, col):
        for i in range(0, self.length):
            self.grid[i][col] = word['word'][i]
        self.word_bank.append(word)

    def make_wordsearch(self):
        word = self.wg.make_wordsearch_word()
        self.length = len(word['word'])
        word_key = word['word']
        row_spot = random.randint(0, self.dim - self.length)
        col_spot = random.randint(0, self.dim - 1)
        placement_attempts = 0

        if word['orientation'] == "HORIZONTAL":
            path = [self.grid[row_spot][i] for i in range(0,self.length)]
            if self.is_placeable(word_key, path):
                self.place_horizontal_word(word, row_spot)
            else:
                while not self.is_placeable(word_key, path) and placement_attempts != self.max_attempts:
                    row_spot = random.randint(0, self.dim - self.length)
                    col_spot = random.randint(0, self.dim - 1)
                    placement_attempts += 1
                else:
                    return
                self.place_vertical_word(word, row_spot, col_spot)
        elif word['orientation'] == 'VERTICAL':
            path = [self.grid[i][col_spot] for i in range(0, self.length)]
            if self.is_placeable(word_key, path):
                self.place_vertical_word(word, row_spot, col_spot)
            else:
                while not self.is_placeable(word_key, path) and placement_attempts != self.max_attempts:
                    row_spot = random.randint(0, self.dim - self.length)
                    col_spot = random.randint(0, self.dim - 1)
                    placement_attempts += 1
                else:
                    return
                self.place_vertical_word(word, row_spot, col_spot)
        else:
            col_spot = random.randint(0, self.dim - self.length)
            path = [self.grid[row_spot + i][col_spot + i] for i in range(0,self.length)]
            if self.is_placeable(word_key, path):
                self.place_diagonal_word(word, row_spot, col_spot)
            else:
                while not self.is_placeable(word_key, path) and placement_attempts != self.max_attempts:
                    row_spot = random.randint(0, self.dim - self.length)
                    col_spot = random.randint(0, self.dim - self.length)
                    placement_attempts += 1
                else:
                    return
                self.place_diagonal_word(word, row_spot, col_spot)


    def __init__(self,dim):
        self.dim = dim
        self.grid  = [[' ' for y in range(x * dim, x * dim + dim)] for x in range(dim)]
        self.word_bank = []
        self.wg = WordSearchGen(dim)
        self.max_attempts = 10
        self.length = 0

        for _ in range(dim - 1):
            self.make_wordsearch()

        pprint(self.word_bank)
        pprint(self.grid, width=self.dim * 10)

def main():
    ws = WordSearchmaker( int(input("Enter a dimension: ")))

if __name__ == '__main__':
    main()