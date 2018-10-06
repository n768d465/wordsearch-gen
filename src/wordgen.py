import random
from wordlist import get_words_from_site

class WordSearchGen:
    def make_wordsearch_word(self):
        return {
            "word": self._pull_word(),
            "orientation": self.orientations[random.randint(0,2)],
            "reversed": random.random() > 0.75
        }

    def get_new_orientation():
        return self.orientations[random.randint(0,2)]

    def _pull_word(self):
        pulled_word = random.choice(self.wordlist)
        self.wordlist.remove(pulled_word)
        return pulled_word

    def get_wordbank(self):
        return [self.make_wordsearch_word() for _ in range(0, self.dim)]

    def __init__(self, dim):
        self.dim = dim
        self.wordlist = get_words_from_site("http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain", dim)
        self.orientations = ("HORIZONTAL", "VERTICAL", "DIAGONAL")
        self.word_bank = []
