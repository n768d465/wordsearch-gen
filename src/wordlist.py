import requests
def get_words_from_site(site, max_length):
    response = requests.get(site)
    return ([word.decode('UTF-8').lower() 
            for word in response.content.splitlines() 
            if len(word) in range (3, max_length) and "'" not in word.decode('UTF-8').lower()])