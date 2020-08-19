from flask import Flask, request

from utils import get_data_by_url, update_words_db, save_db_to_file, count_words_in_data, init_words, get_word_stat_db

app = Flask(__name__)


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
    if data:
        # calculates the words counters
        res = count_words_in_data(data)

    else:
        # check if a url or a text was sent in the request body
        request_data = request.json
        data = request_data["text"] if request_data and "text" in request_data.keys() else None
        url = request_data["url"] if request_data and "url" in request_data.keys() else None

        # if url - get the url file content
        if url:
            # check if an error occurred
            error, res = get_data_by_url(url)
        else:
            res = count_words_in_data(data)
    if res:
        # update the words object
        update_words_db(res)
        # update the json file with the current data
        save_db_to_file()
    return 'SUCCESS'


@app.route('/word_statistics/<word>', methods=["GET"])
def get_word_stat(word):
    stat = get_word_stat_db(word.lower())
    if stat:
        return str(stat)
    else:
        return "0"


if __name__ == '__main__':
    # read the words from the words json file to init the words object
    init_words()
    app.run()
