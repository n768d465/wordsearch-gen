import random
import requests

WORD_LIST = (
    "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
)


def sample_words(max_length):
    response = get_words_from_site(max_length)
    min_word_length = 3
    total_words = 0
    word_range = range(min_word_length, max_length + 1)

    while True:
        w = str(random.choice(response), "UTF-8").lower()
        if "'" in w or len(w) not in word_range:
            continue
        else:
            yield w
            total_words += 1


def get_words_from_site(max_length):
    return requests.get(WORD_LIST).content.splitlines()
