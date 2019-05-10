import random
import requests

WORD_LIST = (
    "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
)


def get_words_from_site():
    res = requests.get(WORD_LIST).content.splitlines()
    return {str(r, "UTF-8").lower() for r in res}


def sample_words(sample_size=50):
    word_list = get_words_from_site()
    while True:
        yield random.sample(word_list, sample_size)


class WordSampler:
    def _is_placeable(self, word, path):
        if len(path) < len(word):
            return False

        if "'" in word or len(word) not in self.word_range:
            return False

        return not any(
            (step != " " and step != char) for (char, step) in zip(word, path)
        )

    def sample_placeable_word(self, path):
        sample = next(self.sample)
        placeables = set(filter(lambda w: self._is_placeable(w, path), sample))

        try:
            return random.choice(random.sample(placeables, 1))
        except Exception:
            return None

    def __init__(self, max_length):
        self.sample = sample_words()
        self.min_word_length = 3
        self.max_length = max_length
        self.word_range = range(self.min_word_length, self.max_length + 1)
