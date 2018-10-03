import requests
def get_words_from_site(site, max_length):
    response = requests.get(site)
    return [word.decode('UTF-8').lower() for word in response.content.splitlines() if len(word) <= max_length]