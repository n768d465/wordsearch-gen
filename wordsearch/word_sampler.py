import random
import requests
import re
import string


def _get_words_from_site():
    word_list = (
        "http://svnweb.freebsd.org/csrg/share/dict"
        "/words?view=co&content-type=text/plain"
    )
    content = requests.get(word_list).content.splitlines()
    word_content = set()
    for c in content:
        word = str(c, "UTF-8").lower()
        if not re.search(f"[{string.punctuation}]", word):
            word_content.add(word)

    return word_content


def _sample_words(word_range, sample_size=50):
    word_list = _get_words_from_site()
    li = [w for w in word_list if len(w) in word_range]
    while True:
        yield random.sample(li, sample_size)


def _is_placeable(word, path):
    return not any((step != " " and step != char) for (char, step) in zip(word, path))


def _filter_criteria(word_item, path):
    word = word_item["word"]
    word = word[::-1] if word_item["reversed"] else word
    if len(word) > len(path):
        return False

    return _is_placeable(word, path)


def create_sampler(max_length):
    word_range = range(3, max_length + 1)
    word_sample_iter = _sample_words(word_range)

    def sample_one_placeable(path):
        word_sample = next(word_sample_iter)
        sample = [
            {"word": w, "reversed": random.choice([True, False]), "positions": []}
            for w in word_sample
        ]

        placeables = list(filter(lambda w: _filter_criteria(w, path), sample))

        try:
            return random.choice(placeables)
        except Exception:
            return None

    return sample_one_placeable

