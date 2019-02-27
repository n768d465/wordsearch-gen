import random
import requests
from collections import defaultdict
import json

WORD_LIST = (
    "https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json"
)


def pull_word(word_list):
    pulled_word = random.sample(word_list, 1)[0]
    word_list.remove(pulled_word)
    return pulled_word


def get_wordbank(max_length):
    word_list = get_local_words(max_length)
    all_words = defaultdict(lambda: [])

    for w in word_list:
        if len(w) <= max_length:
            all_words[len(w)].append(w)

    return all_words


def get_words_from_site(max_length):
    response = requests.get(WORD_LIST)
    words = set()
    min_word_length = 3
    word_range = range(min_word_length, max_length + 1)
    for word in response.content.splitlines():
        if len(word) in word_range:
            words.add(word)

    return words


def get_local_words(max_length):
    with open("words_dictionary.json") as outf:
        words = json.load(outf)
        return set(words.keys())
