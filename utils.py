import json
import requests


def get_data_by_url(url):
    try:
        r = requests.get(url, allow_redirects=True)
        return None, r.content
    except requests.exceptions.RequestException as e:
        return "error", {}


def count_words_in_data(data):
    res = {}
    for word in data.split(" "):
        # remove all unwonted chars
        word = ''.join(c for c in word if c not in '0123456789.-!@#$%^&*()_+{}",<>?~`\\ \n')
        if word in res.keys():
            res[word] += 1
        else:
            res[word] = 1
    return res


def update_words_db(current_words, new_data):
    for word, counter in new_data.items():
        if word in current_words.keys():
            current_words[word] += counter
        else:
            current_words[word] = counter


def save_db_to_file(current_words):
    with open('static/words_db.json', 'w') as words_json_file:
        json.dump(current_words, words_json_file)
