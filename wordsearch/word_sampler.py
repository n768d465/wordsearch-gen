import random


def sample_placeable_word(category_list, min_length, max_length, path):
    choice = str(random.choice(range(min_length, max_length)))
    sample = [WordItem(w) for w in category_list.get(choice, [])]
    placeables = list(filter(lambda w: w and _filter_criteria(w, path), sample))

    try:
        return random.choice(placeables)
    except IndexError:
        return None


class WordItem(object):
    @property
    def word(self):
        return self._word[::-1] if self.reversed else self._word

    @word.setter
    def word(self, value):
        self._word = value

    def __init__(self, word):
        self.word2 = word
        self.word = word
        self.reversed = random.choice([True, False])
        self.positions = []


def _filter_criteria(word_item: WordItem, path: "list[str]") -> bool:
    word = word_item.word
    if len(word) > len(path):
        return False

    return not any((step != " " and step != char) for (char, step) in zip(word, path))
