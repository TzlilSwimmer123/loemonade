import json

from flask import Flask, request

from utils import get_data_by_url, update_words_db, save_db_to_file, count_words_in_data

app = Flask(__name__)

words = None


@app.route('/count', methods=["POST"])
def count_words():
    encoding = 'utf-8'
    data = None
    # check if a file was sent in the post body
    if request.files:
        # get the file
        file_to_count = request.files['file']
        # read and encode the file
        try:
            # decode bytes to string after reading the file
            data = file_to_count.read().decode(encoding)
        except Exception as file_exception:
            print(file_exception)

    else:
        # check if a url or a text was sent in the request body
        request_data = request.json
        data = request_data["text"] if "text" in request_data.keys() else None
        url = request_data["url"] if "url" in request_data.keys() else None

        # if url - get the url file content
        if url:
            # check if an error occurred
            error, data = get_data_by_url(url)
            if not error:
                try:
                    # decode bytes to string
                    data = data.decode(encoding)
                except Exception as get_file_exception:
                    print(get_file_exception)

    if data:
        # calculates the words counters
        res = count_words_in_data(data)
        # update the words object
        update_words_db(words, res)
        # update the json file with the current data
        save_db_to_file(words)
    return 'SUCCESS'


@app.route('/word_statistics/<word>', methods=["GET"])
def get_word_stat(word):
    stat = words[word] if word in words.keys() else None
    if stat:
        return str(stat)
    else:
        return "0"


if __name__ == '__main__':
    # read the words from the words json file to init the words object
    try:
        with open('static/words_db.json', 'r') as words_json_file:
            words = json.load(words_json_file)
    except Exception as e:
        print(e)
    app.run()
