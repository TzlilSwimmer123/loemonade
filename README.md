# loemonade

At the moment we supply 2 apis:

1)

POST request /count <br />
    1. you can send a file that its key is "file" <br />
    2. you can send a json body as follows <br />
    {
        "text": "The text that should be calculated"
    }<br />
    or
    {
        "url": "http://theurlthat.thefile.isin"
    }<br />
    don't send them both!<br />
    examples:
    {
        "url": "https://www.w3.org/TR/PNG/iso_8859-1.txt"
    }
    {
        "text": "Hi! My name is (what?), my name is (who?), my name is Slim Shady"
    }<br />
    
Make sure all of the content is in English!<br />

2)

GET request /word_statistics/<word><br />
the word is a the word you want to check the stats of it. 
example:
/word_statistics/Shady