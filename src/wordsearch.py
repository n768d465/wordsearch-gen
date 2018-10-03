from pprint import pprint
from wordgen import WordSearchGen

def make_wordsearch(dim):
    grid  = [[y  for y in range(x * dim, x * dim + dim)] for x in range(dim)]
    pprint(grid)

def main():
    wg = WordSearchGen(5)
    make_wordsearch(5)

if __name__ == '__main__':
    main()

