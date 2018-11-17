import random
import requests

WORD_LIST = (
    "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
)


def pull_word(word_list):
    pulled_word = random.sample(word_list, 1)[0]
    word_list.remove(pulled_word)
    return pulled_word


def get_wordbank(dim):
    word_list = get_words_from_site(WORD_LIST, dim)
    orientations = ("HORIZONTAL", "VERTICAL", "DIAGONAL")

    return [
        {
            "word": pull_word(word_list),
            "orientation": orientations[random.randint(0, 2)],
            "reversed": random.random() > 0.70,
        }
        for _ in range(0, dim)
    ]


def get_words_from_site(site, max_length):
    response = requests.get(site)
    return {
        word.decode("UTF-8").lower()
        for word in response.content.splitlines()
        if len(word) in range(3, max_length + 1)
        and "'" not in word.decode("UTF-8").lower()
    }
