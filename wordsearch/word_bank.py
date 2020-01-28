import random
import requests


def _get_words_from_site():
    word_list = (
        "http://svnweb.freebsd.org/csrg/share/dict"
        "/words?view=co&content-type=text/plain"
    )
    res = requests.get(word_list).content.splitlines()
    return {str(r, "UTF-8").lower() for r in res}


def _sample_words(word_range, sample_size=50):
    word_list = _get_words_from_site()
    li = [w for w in word_list if len(w) in word_range]
    while True:
        yield random.sample(li, sample_size)


class WordSampler:
    def _is_placeable(self, word_item, path):
        word = word_item["word"]
        word = word[::-1] if word_item["reversed"] else word

        return not any(
            (step != " " and step != char) for (char, step) in zip(word, path)
        )

    def sample_placeable_word(self, path):
        word_sample = next(self.sample)
        sample = [
            {"word": w, "reversed": random.choice([True, False]), "positions": []}
            for w in word_sample
        ]
        placeables = list(filter(lambda w: len(path) > len(w), sample))
        placeables = list(filter(lambda w: self._is_placeable(w, path), placeables))

        try:
            return random.choice(random.sample(placeables, 1))
        except Exception:
            return None

    def __init__(self, max_length):
        self.word_range = range(3, max_length + 1)
        self.sample = _sample_words(self.word_range)
