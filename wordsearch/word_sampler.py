import random
import requests
import re
import string
from collections import defaultdict


class Sampler:
    def __call__(self, path):
        sample = [
            {"word": w, "reversed": random.choice([True, False]), "positions": []}
            for w in self.word_list[random.choice(self.word_range)]
        ]

        placeables = list(filter(lambda w: _filter_criteria(w, path), sample))
        try:
            return random.choice(placeables)
        except Exception:
            return None

    def __init__(self, min_length, max_length):
        self.word_range = range(min_length, max_length + 1)
        self.word_list = _get_words_from_site()


def _get_words_from_site():
    word_list = (
        "http://svnweb.freebsd.org/csrg/share/dict"
        "/words?view=co&content-type=text/plain"
    )
    content = requests.get(word_list).content.splitlines()
    word_content = defaultdict(list)
    for c in content:
        word = str(c, "UTF-8").lower()
        if not re.search(f"[{string.punctuation}]", word):
            word_content[len(word)].append(word)

    for k in word_content.keys():
        random.shuffle(word_content[k])

    return word_content


def _filter_criteria(word_item, path):
    word = word_item["word"]
    word = word[::-1] if word_item["reversed"] else word
    if len(word) > len(path):
        return False

    return _is_placeable(word, path)


def _is_placeable(word, path):
    return not any((step != " " and step != char) for (char, step) in zip(word, path))
