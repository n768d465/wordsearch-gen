import random
import requests

WORD_LIST = (
    "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
)


def is_placeable(word, path):
    if len(path) < len(word):
        return False

    if all(c != " " for c in path):
        return False

    return not any((step != " " and step != char) for (char, step) in zip(word, path))


def get_words_from_site():
    res = requests.get(WORD_LIST).content.splitlines()
    words = {str(r, "UTF-8").lower() for r in res}

    while len(words):
        yield random.sample(words, 1)[0]


class WordBank:
    def placeable_words(self, path):
        w = next(self.cached)
        if len(w) <= len(path) and is_placeable(w, path):
            if "'" not in w and len(w) in self.word_range:
                return w
        else:
            return None

    def __init__(self, max_length):
        self.cached = get_words_from_site()
        self.min_word_length = 3
        self.max_length = max_length
        self.word_range = range(self.min_word_length, self.max_length + 1)

