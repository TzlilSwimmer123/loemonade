import json
import requests
import shutil

words = None


def init_words():
    global words
    try:
        with open('static/words_db.json', 'r') as words_json_file:
            words = json.load(words_json_file)
    except Exception as e:
        print(e)


def get_data_by_url(url):
    try:
        # get the content of the file
        with requests.get(url, stream=True) as r:
            data = r.content.decode('utf-8')
            content_count = count_words_in_data(data)
            update_words_db(content_count)
            save_db_to_file()
        return None, None
    except (requests.exceptions.RequestException, UnicodeDecodeError) as e:
        return "error", {}


def count_words_in_data(data):
    data = data.replace("\n", " ")
    data = data.replace("\t", " ")

    chars_to_replace = "0123456789.-!@#$%^&*()_+{}:[];\"',=<>?~`\\ "
    res = {}
    for word in data.split(" "):
        word_parts = word.split("-")
        for part in word_parts:
            # remove all unwonted chars
            for char in chars_to_replace:
                part = part.replace(char, "")
            part = part.lower()
            if part in res.keys():
                res[part] += 1
            else:
                res[part] = 1

    return res


def update_words_db(new_data):
    for word, counter in new_data.items():
        if word in words.keys():
            words[word] += counter
        else:
            words[word] = counter


def save_db_to_file():
    with open('static/words_db.json', 'w') as words_json_file:
        json.dump(words, words_json_file)


def get_word_stat_db(word):
    stat = words[word] if word in words.keys() else None
    return stat
