# loemonade

At the moment we supply 2 apis:

1)

POST request /count
    1. you can send a file that its key is "file"
    2. you can send a json body as follows
    {
        "text": "The text that should be calculated"
    }
    or
    {
        "url": "http://theurlthat.thefile.isin"
    }
    don't send them both!
    examples:
    {
        "url": "https://www.w3.org/TR/PNG/iso_8859-1.txt"
    }
    {
        "text": "Hi! My name is (what?), my name is (who?), my name is Slim Shady"
    }
    
Make sure all of the content is in English!

2)

GET request /word_statistics/<word>
the word is a the word you want to check the stats of it. 
example:
/word_statistics/Shady