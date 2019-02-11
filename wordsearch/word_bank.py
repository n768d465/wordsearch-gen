import random
import requests
from collections import defaultdict

WORD_LIST = (
    "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
)


def pull_word(word_list):
    pulled_word = random.sample(word_list, 1)[0]
    word_list.remove(pulled_word)
    return pulled_word


def get_wordbank(dim):
    word_list = get_words_from_site(dim)
    all_words = defaultdict(lambda: [])

    for w in word_list:
        if len(w) <= 11:
            all_words[len(w)].append(w)

    return all_words


def get_words_from_site(max_length):
    response = requests.get(WORD_LIST)
    return {
        word.decode("UTF-8").lower()
        for word in response.content.splitlines()
        if len(word) in range(3, max_length + 1)
        and "'" not in word.decode("UTF-8").lower()
    }
